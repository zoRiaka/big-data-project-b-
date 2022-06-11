# big-data-project-b-
Task b of a project for the UCU Big Data Processing course.

The results of queries are in Screenshots folder

## Explanations:

In order to manipulate with the data stream I used Kafka. It has many advantages, one of it being able to run processes of producer and consumer simultaneously, which is great for the optimization especially with big data sets. And for my database tables I used Cassandra. Cassandra is a relatively simple instrument that allows us to store our data and execute simple queries. There is also a Cassandra support in python which is great for creating the app.

## Usage:

In order to run kafka writer execute:

```
bash run-cluster.sh
bash create-topic.sh
bash kafka_write/build-run.sh
```
In order to run kafka consumer and cassandra writer execute:
```
bash kafka_cassandra/run-cassandra-node.sh
bash kafka_cassandra/keyspace-tables.sh
bash kafka_cassandra/build-run.sh
```
In order to run app execute:

```
bash cassandra_app/build-run.sh
```

To shutdown all the containers and cluster run all shutdown scripts.

## NOTE:

Example of queries:

http://172.26.0.5:5000queries?query=1


http://172.26.0.5:5000/queries?query=2&user_id=327734


http://172.26.0.5:5000/queries?query=3&domain=commons.wikimedia.org


http://172.26.0.5:5000/queries?query=4&page_id=119180432


http://172.26.0.5:5000/queries?query=5&start=2022-06-10&end=2022-07-11

