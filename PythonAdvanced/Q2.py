import boto3

session = boto3.Session(profile_name="Piyush")

sts_client = session.client('sts')

response_b = sts_client.assume_role(
    RoleArn="arn:aws:iam::488182246720:role/AccountBRole",
    RoleSessionName="sessionB"
)

credentials_b = response_b['Credentials']

session_b = boto3.Session(
    aws_access_key_id=credentials_b['AccessKeyId'],
    aws_secret_access_key=credentials_b['SecretAccessKey'],
    aws_session_token=credentials_b['SessionToken']
)

sts_b = session_b.client('sts')

response_c = sts_b.assume_role(
    RoleArn="arn:aws:iam::691768189243:role/AccountCRole",
    RoleSessionName="sessionC"
)

credentials_c = response_c['Credentials']

session_c = boto3.Session(
    aws_access_key_id=credentials_c['AccessKeyId'],
    aws_secret_access_key=credentials_c['SecretAccessKey'],
    aws_session_token=credentials_c['SessionToken']
)

ec2_client = session_c.client('ec2')

response = ec2_client.describe_instances()

print("EC2 Instances in Account C:")
print(response)