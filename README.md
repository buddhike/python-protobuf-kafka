# Quick Example Read/Write Protobuf Data From/To Kafka Using Python

## Steps

- Use `protoc --python_out=. ./person.proto` to generate python code for serialization and deserialization.
- Install dependencies
    ```
      pip install protobuf
      pip install confluent-kafka
    ```
  
- Inspect the code in `main.py` to learn how to read/write messages.
  `read_person` method is deliberately reading only one message for brevity. Streaming applications must use a poll loop to continuously receive messages from stream. An example of a poll loop can be found [here](https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html#python-demo-code).
