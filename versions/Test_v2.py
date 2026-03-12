import boto3
s3_resource = boto3.resource('s3')
print(s3_resource)

for bucket in s3_resource.buckets.all():
    print(bucket.name)