import boto3
import csv

iam = boto3.client("iam")
ec2 = boto3.client("ec2")

with open("iam_roles_admin_access.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IAMRoleName", "PolicyName"])

    roles = iam.list_roles()["Roles"]

    for role in roles:
        role_name = role["RoleName"]

        policies = iam.list_attached_role_policies(RoleName=role_name)["AttachedPolicies"]

        for policy in policies:
            if policy["PolicyName"] == "AdministratorAccess":
                writer.writerow([role_name, policy["PolicyName"]])

print("IAM role check completed")

with open("iam_user_mfa_status.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IAMUserName", "MFAEnabled"])

    users = iam.list_users()["Users"]

    for user in users:
        username = user["UserName"]

        mfa = iam.list_mfa_devices(UserName=username)["MFADevices"]

        mfa_enabled = len(mfa) > 0

        writer.writerow([username, mfa_enabled])

print("MFA check completed")


with open("security_group_risk.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["SGName", "Port", "AllowedIP"])

    sgs = ec2.describe_security_groups()["SecurityGroups"]

    for sg in sgs:
        sg_name = sg["GroupName"]

        for permission in sg["IpPermissions"]:

            port = permission.get("FromPort")

            if port in [22, 80, 443]:

                for ip in permission["IpRanges"]:

                    if ip["CidrIp"] == "0.0.0.0/0":
                        writer.writerow([sg_name, port, "0.0.0.0/0"])

print("Security group check completed")


with open("unused_keypairs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["KeyPairName"])

    keypairs = ec2.describe_key_pairs()["KeyPairs"]

    instances = ec2.describe_instances()["Reservations"]

    used_keys = set()

    for r in instances:
        for i in r["Instances"]:
            if "KeyName" in i:
                used_keys.add(i["KeyName"])

    for key in keypairs:
        if key["KeyName"] not in used_keys:
            writer.writerow([key["KeyName"]])

print("Unused key pair check completed")