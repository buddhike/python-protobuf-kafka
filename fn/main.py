from person_pb2 import Person

def handler(event, context):
    print("==========BATCH START==========")
    for r in event["records"] or []:
       for t in r:
          p = Person()
          p.ParseFromString(r[t]["value"])
          print(p.id, p.name, p.email)

    print("=========BATCH END==========")