import json
from time import sleep
from kafka import KafkaProducer, KafkaConsumer
import csv
import requests
from json import dumps, loads
from datetime import date, timedelta
import sys
import random

producer = KafkaProducer(bootstrap_servers='kafka-server:9092', api_version=(2, 0, 2),
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
print("connected to producer")

s = requests.Session()
url = "https://stream.wikimedia.org/v2/stream/page-create"

try:
    with s.get(url, stream=True) as r:
        for row in r.iter_lines(decode_unicode=True):
            if row and row.split(':')[0] == "data":
                # row = loads(dumps(str(row.decode('utf-8').replace("\"", "").replace("\n", "").replace("\\", "")))[0])
                result = producer.send('my-topic', str(loads(row[5:])))
                sleep(0.01)
        producer.flush()
except KeyboardInterrupt:
    sys.exit(0)
