from pprint import pprint

import kinesis_stream as ks


def create_stream(client, stream_name, shard_count=1):
    ks.create_stream(client, stream_name, shard_count)
    ks.wait_for_stream_to_be_active(client, stream_name)


def create_mock_records(client, qty):
    ks.create_stream(client, stream_name, 1)
    ks.wait_for_stream_to_be_active(client, stream_name)
    ks.write_mock_orders_to_aws_kinesis(client, stream_name, qty)


def delete_stream(client, stream_name):
    ks.delete_stream(client, stream_name)
    ks.waiting_for_stream_to_be_deleted(client, stream_name)


def test_stream():
    global stream_name
    client = ks.create_client()
    stream_name = "order1"
    create_stream(client=client, stream_name=stream_name, shard_count=2)
    create_mock_records(client, 10)
    shards = ks.get_shards(client, stream_name)
    for shard in shards:
        iterator = ks.get_shard_iterator(client, stream_name, shard)
        print('-' * 6 + ' ' + shard + ' ' + '-' * 56)
        records = ks.get_records(client, iterator)
        for record in records:
            print(record['Data'])
        print('\nNumber of records: ' + str(len(records)) + '\n')
    pprint(client.describe_stream_summary(StreamName=stream_name))
    delete_stream(client, stream_name)

if __name__ == '__main__':
    test_stream()
