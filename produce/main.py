from person_pb2 import Person
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic

import os
import uuid


def handler(event, context):
    print("writing a new record to kafka")
    for i in range(10):
        person = Person()
        person.id = i
        person.name = str(uuid.uuid4())
        person.email = "alice@amazon.com"
        # Serialize person to protobuf bytes
        msg = person.SerializeToString()

        # Write bytes to topic
        conf = {"bootstrap.servers": os.getenv("BOOTSTRAP_SERVERS"), "client.id": "producer"}
        admin = AdminClient(conf)
        try:
            admin.create_topics([NewTopic("pb", 1, 1)])
        except Exception as e:
            print("could not create the topic", e)

        producer = Producer(conf)
        producer.produce("pb", msg)
        print(producer.flush())
        print("a new person added to stream")
