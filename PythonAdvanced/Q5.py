import boto3
from datetime import datetime, timedelta, timezone

ec2 = boto3.client("ec2")
cloudwatch = boto3.client("cloudwatch")
rds = boto3.client("rds")
lambda_client = boto3.client("lambda")
s3 = boto3.client("s3")

print("---- Cost Optimization Report ----")


end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(days=30)


print("\nEC2 Instances with Low CPU Utilization (<10%)")

instances = ec2.describe_instances()

for reservation in instances["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]

        metrics = cloudwatch.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName="CPUUtilization",
            Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
            StartTime=start_time,
            EndTime=end_time,
            Period=86400,
            Statistics=["Average"]
        )

        datapoints = metrics["Datapoints"]

        if datapoints:
            avg_cpu = sum(d["Average"] for d in datapoints) / len(datapoints)

            if avg_cpu < 10:
                print(f"Low CPU EC2 Instance: {instance_id} (Avg CPU: {avg_cpu:.2f}%)")


print("\nIdle RDS Instances")

dbs = rds.describe_db_instances()["DBInstances"]

for db in dbs:
    db_id = db["DBInstanceIdentifier"]

    metrics = cloudwatch.get_metric_statistics(
        Namespace="AWS/RDS",
        MetricName="DatabaseConnections",
        Dimensions=[{"Name": "DBInstanceIdentifier", "Value": db_id}],
        StartTime=end_time - timedelta(days=7),
        EndTime=end_time,
        Period=86400,
        Statistics=["Average"]
    )

    datapoints = metrics["Datapoints"]

    if datapoints:
        avg_conn = sum(d["Average"] for d in datapoints) / len(datapoints)

        if avg_conn == 0:
            print(f"Idle RDS Instance: {db_id}")


print("\nLambda Functions Not Invoked in 30 Days")

functions = lambda_client.list_functions()["Functions"]

for func in functions:
    func_name = func["FunctionName"]

    metrics = cloudwatch.get_metric_statistics(
        Namespace="AWS/Lambda",
        MetricName="Invocations",
        Dimensions=[{"Name": "FunctionName", "Value": func_name}],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,
        Statistics=["Sum"]
    )

    datapoints = metrics["Datapoints"]

    total_invocations = sum(d["Sum"] for d in datapoints)

    if total_invocations == 0:
        print(f"Unused Lambda Function: {func_name}")

print("\nUnused / Empty S3 Buckets")

buckets = s3.list_buckets()["Buckets"]

for bucket in buckets:
    bucket_name = bucket["Name"]

    objects = s3.list_objects_v2(Bucket=bucket_name)

    if "Contents" not in objects:
        print(f"Empty S3 Bucket: {bucket_name}")