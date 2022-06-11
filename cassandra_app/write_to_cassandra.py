import pandas as pd
from datetime import datetime
import gzip
import shutil
from kafka import KafkaProducer, KafkaConsumer
import csv
from json import loads
import ast

import numpy as np


class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        from cassandra.cluster import Cluster
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)

    def execute(self, query):
        self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def insert_tables(self):
        query1 = "INSERT INTO by_user(user_id, user_name, time_date) VALUES (?, ?, ?)"
        prepared1 = self.session.prepare(query1)

        query2 = "INSERT INTO by_page(page_id, page_uri, page_domain, user_id) VALUES (?, ?, ?, ?)"
        prepared2 = self.session.prepare(query2)

        for msg in consumer:
            msg = ast.literal_eval(msg.value)
            try:
                page_id = msg['page_id']
                page_uri = msg['meta']['uri']
                domain = msg['meta']['domain']
                user_id = msg['performer']['user_id']
                user_name = msg['performer']['user_text']
                time = datetime.strptime(msg['rev_timestamp'], '%Y-%m-%dT%H:%M:%SZ')
                self.session.execute(prepared1, (str(user_id), str(user_name), time))
                self.session.execute(prepared2, (str(page_id), str(page_uri), str(domain), str(user_id)))

            except:
                pass

    def query_1(self):
        query = "select page_domain from by_page;"
        rows = self.session.execute(query)
        myset = set(list(rows))
        return list(myset)

    def query_2(self, user_id):
        query = " select page_id from by_page where user_id = '%s';" % user_id
        rows = self.session.execute(query)
        return list(rows)

    def query_3(self, domain):
        query = "select count(*) from by_page where page_domain = '%s' allow filtering;" % domain
        rows = self.session.execute(query)
        return list(rows)

    def query_4(self, page_id):
        query = " select page_uri from by_page where page_id = '%s' allow filtering;" % page_id
        rows = self.session.execute(query)
        return list(rows)

    def query_5(self, start, end):
        query = " select user_id, user_name, count(user_id) from by_user where time_date > '%s' and time_date < '%s' group by user_id allow filtering;" % (
        start, end)
        rows = self.session.execute(query)
        return list(rows)


if __name__ == '__main__':
    host = 'node1'
    port = 9042
    keyspace = 'my_keyspace'
    consumer = KafkaConsumer('my-topic', bootstrap_servers='kafka-server:9092', api_version=(2, 0, 2),
                             value_deserializer=lambda x: loads(x.decode('utf-8')))

    client = CassandraClient(host, port, keyspace)
    client.connect()
    client.insert_tables()
    client.close()
