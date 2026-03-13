import boto3
import csv

def get_all_regions():
    ec2 = boto3.client("ec2")
    regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
    return regions


def get_instance_types(region):
    ec2 = boto3.client("ec2", region_name=region)
    
    instance_types = set() 
    paginator = ec2.get_paginator("describe_instance_types")

    for page in paginator.paginate():
        for instance in page["InstanceTypes"]:
            instance_types.add(instance["InstanceType"])

    return instance_types


def write_to_csv(data, filename="ec2_instance_types.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["region", "instance_type"])

        for region, instance_types in data.items():
            for itype in instance_types:
                writer.writerow([region, itype])


def main():
    regions = get_all_regions()
    result = {}

    for region in regions:
        print(f"Fetching instance types for {region}...")
        result[region] = get_instance_types(region)

    write_to_csv(result)
    print("CSV file created successfully: ec2_instance_types.csv")


if __name__ == "__main__":
    main()