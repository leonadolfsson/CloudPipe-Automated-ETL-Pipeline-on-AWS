import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')

    job_name = 's3-glue-s3' 
    try:
        response = glue.start_job_run(JobName=job_name)
        return {
            'statusCode': 200,
            'body': f"Started Glue job '{job_name}' with JobRunId: {response['JobRunId']}"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Failed to start Glue job: {str(e)}"
        }

