import boto3

# To select the aws service
session = boto3.Session(profile_name ="dev_etl")

s3 =session.client('s3')
bucket_list = s3.list_buckets()

print('Existing buckets:')
for bucket in bucket_list['Buckets']:
    print(f'  {bucket["Name"]}')