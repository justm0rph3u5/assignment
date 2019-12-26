import boto3

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def upload_file(file_name, bucket):
    # type: (object, object) -> object
    """
    Function to upload a file to an S3 bucket
    """
    objectname = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, objectname)
    return response

def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output = f"downloads/{file_name}"
    s3.Bucket(bucket).download_file(file_name, output)

    return output

def delete_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output=s3.Bucket(bucket).Object(file_name).delete()
    return output

def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3 = boto3.client('s3')
    contents = []
    for item in s3.list_objects(Bucket=bucket)['Contents']:
            print(item)
            contents.append(item)
    return contents

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS