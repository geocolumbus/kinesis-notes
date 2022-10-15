# AWS Kinesis Datastreams

Amazon Kinesis Data Streams is a managed service that scales elastically for real-time processing of streaming big data.

## Usage

### Set up AWS access

```text
$ cat ~/.aws/credentials
[default]
aws_access_key_id = AKIA...
aws_secret_access_key = tPth...
```

```text
$ cat ~/.aws/config
[default]
region=us-east-2
output=json
account=0820...
cli_pager=
```

### Set up the python environment

```bash
$ python -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```

### Run the application
$ python main.py

## Reference
* [aws kinesis documentation](https://docs.aws.amazon.com/kinesis/index.html)
* [boto3 kinesis](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html)
* [kinesis size & limits](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html)
* [kinesis pricing](https://aws.amazon.com/kinesis/data-streams/pricing/)