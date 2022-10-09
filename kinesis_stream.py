import boto3
import json


def create_client(region_name="us-east-2"):
    print("Creating client in region: " + region_name)
    client = boto3.client('kinesis', region_name=region_name)
    return client


def stream_exists(client, stream_name):
    response = client.list_streams()
    return stream_name in response["StreamNames"]


def create_stream(client, stream_name, shard_count=1):
    if stream_exists(client, stream_name):
        print("Cannot create stream that already exists: " + stream_name)
        return
    print("Creating stream: " + stream_name)
    response = client.create_stream(StreamName=stream_name, ShardCount=shard_count)


def wait_for_stream_to_be_active(client, stream_name):
    print("Waiting for stream to be active: " + stream_name)
    waiter = client.get_waiter('stream_exists')
    waiter.wait(StreamName=stream_name)
    print("Stream is active: " + stream_name)


def delete_stream(client, stream_name):
    if not stream_exists(client, stream_name):
        print("Cannot delete stream that does not exist: " + stream_name)
        return
    print("Deleting stream: " + stream_name)
    response = client.delete_stream(StreamName=stream_name)


def waiting_for_stream_to_be_deleted(client, stream_name):
    print("Waiting for stream to be deleted: " + stream_name)
    waiter = client.get_waiter('stream_not_exists')
    waiter.wait(StreamName=stream_name)
    print("Stream is deleted: " + stream_name)


def write_mock_orders_to_aws_kinesis(client, stream_name, qty):
    from create_order import generate_random_order
    print("Writing " + str(qty) + " mock orders to stream: " + stream_name)

    for i in range(0, qty):
        order = generate_random_order()
        order["id"] = str(i)
        try:
            response = client.put_record(StreamName=stream_name, Data=json.dumps(order),
                                         PartitionKey=order["id"])
        except Exception as e:
            print(e)


def get_streams(client):
    response = client.list_streams()
    return response["StreamNames"]


def get_shards(client, stream_name):
    response = client.describe_stream(StreamName=stream_name)
    shards = response["StreamDescription"]["Shards"]
    shard_ids = []
    for shard in shards:
        shard_ids.append(shard["ShardId"])
    return shard_ids


def get_shard_iterator(client, stream_name, shard_id):
    response = client.get_shard_iterator(StreamName=stream_name, ShardId=shard_id,
                                         ShardIteratorType="TRIM_HORIZON")
    return response["ShardIterator"]


def get_records(client, shard_iterator):
    response = client.get_records(ShardIterator=shard_iterator)
    return response["Records"]
