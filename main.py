from person_pb2 import Person
from confluent_kafka import Producer, Consumer


def write_person():
   person = Person()
   person.id = 1
   person.name = "Alice Smith"
   person.email = "alice@amazon.com"
   # Serialize person to protobuf bytes
   msg = person.SerializeToString()

   # Write bytes to topic
   conf = {"bootstrap.servers": "localhost:9092", "client.id": "producer"}
   producer = Producer(conf)
   producer.produce("pb", msg)
   print(producer.flush())
   print("a new person added to stream")


def read_person():
   conf = {'bootstrap.servers': "localhost:9092",
           'group.id': "pb_consumer",
           'auto.offset.reset': 'smallest'}

   consumer = Consumer(conf)
   consumer.subscribe(["pb"])
   msg = consumer.poll(5)
   # Show that message body is an array of bytes
   print("message body type is: %s", type(msg.value()))

   # Use message payload to initialize a Person instance
   p = Person()
   p.ParseFromString(msg.value())
   print(p.id, p.name, p.email)

if __name__ == '__main__':
   write_person()
   read_person()
