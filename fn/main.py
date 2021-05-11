import base64

from person_pb2 import Person


def handler(event, context):
    print("==========BATCH START==========")

    for t in event["records"] or []:
        print("topic", t)
        for r in event["records"][t]:
            p = Person()
            p.ParseFromString(base64.b64decode(r["value"]))
            print(p.id, p.name, p.email)

    print("=========BATCH END==========")

