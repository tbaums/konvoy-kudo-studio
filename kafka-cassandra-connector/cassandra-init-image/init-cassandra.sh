#!/bin/bash

cassandra_instance=$CASSANDRA_ENDPOINT

sleep 1

cqlsh ${cassandra_instance} --execute "CREATE KEYSPACE research WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};" || echo "Keyspace exists"

sleep 1

cqlsh ${cassandra_instance} --execute "USE research; CREATE TABLE coordinates (uid int PRIMARY KEY, x decimal, y decimal);" || echo "Table exists"
