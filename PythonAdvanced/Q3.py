import boto3

ec2 = boto3.client("ec2")

regions = ec2.describe_regions()["Regions"]

regions_with_resources = []

for r in regions:
    region_name = r["RegionName"]
    
    ec2_regional = boto3.client("ec2", region_name=region_name)


    response = ec2_regional.describe_instances()

    if response["Reservations"]:
        regions_with_resources.append(region_name)


print("Regions where customer has resources:")

for region in regions_with_resources:
    print(region)