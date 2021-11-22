import boto3

def lambda_handler(envent,context):
    
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(Filters = [{'Name': 'key-name', 'Values':['ec2-key-name']}])
    reservations = response.get("Reservations")
    for res in reservations:
        for ins in res["Instances"]:
            instance_id = ins["InstanceId"]
            respp = ec2_client.stop_instances(InstanceIds=[instance_id])
            print(respp)
