docker exec -it node1 cqlsh -e "CREATE KEYSPACE my_keyspace WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };
USE my_keyspace;
CREATE TABLE by_user (user_id text, user_name text, time_date date, PRIMARY KEY (user_id, time_date));
CREATE TABLE by_page (page_id text, page_uri text, page_domain text, user_id text, PRIMARY KEY (user_id, page_domain));
EXIT;"
