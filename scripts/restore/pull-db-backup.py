import ibm_boto3
import os
from ibm_botocore.client import Config, ClientError

# Constants for IBM COS values
COS_ENDPOINT = os.environ['ENDPOINT' ]
COS_API_KEY_ID = os.environ['API_KEY']
COS_AUTH_ENDPOINT = os.environ['AUTH_ENDPOINT']
COS_RESOURCE_CRN = os.environ['RESOURCE_CRN']
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_RESOURCE_CRN,
    ibm_auth_endpoint=COS_AUTH_ENDPOINT,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)
def get_item(bucket_name, item_name):
    try:
        file = cos.Object(bucket_name, item_name).get()
        txt = str(file["Body"].read().decode('UTF-8'))
        path = "databackup.sql"
        with open(path, "w") as file:
           file.write(txt)
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve file contents: {0}".format(e))

get_item(os.environ['BUCKET_NAME'],os.environ['BACKUP_FILE']);
