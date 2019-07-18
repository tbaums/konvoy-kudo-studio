# Konvoy + Kudo Studio

_NB: This is very much a work in progress. Suggestions, constructive criticism, and (especially) PRs are most welcome!_

Tested with Konvoy v0.4.0 and Kudo v0.3.2 on AWS. 


## Initial setup

### Deploy Kudo Kafka
1. `curl -O https://raw.githubusercontent.com/tbaums/kudo-kafka-etl/master/install-kudo-prereqs.sh`
1. `sh install-kudo-prereqs.sh`
1. `kubectl kudo install zookeeper --instance=zk`
1. `kubectl kudo install kafka --instance=kafka --parameter ZOOKEEPER_URI=zk-zookeeper-0.zk-hs:2181,zk-zookeeper-1.zk-hs:2181,zk-zookeeper-2.zk-hs:2181 --parameter ZOOKEEPER_PATH=/small -p BROKERS_COUNTER=3`

### Deploy Kafka Client API, Svelte front-end, and Dummy Actors
1. `kubectl apply -f https://raw.githubusercontent.com/tbaums/kudo-kafka-etl/master/kudo-kafka-app/kafka-client-api.yaml`
1. `kubectl apply -f https://raw.githubusercontent.com/tbaums/svelte-client/master/svelte-client.yaml`
1. `curl -O https://raw.githubusercontent.com/tbaums/svelte-client/master/dummy-actors/kafka-dummy-actor.yaml`
1. Edit `kafka-dummy-actor.yaml` and set `KAFKA_API_URL` to your AWS ELB.
1. `kubectl apply -f kafka-dummy-actor.yaml`


### Navigate to Svelte UI
1. Visit \<your AWS elb\>/svelte
1. Click 'Manufactoring & IoT' in the Nav bar
1. Click button 'Click me to start fetch'
1. Observe a single actor on the map (left) and in the actor list (on right).
1. Run `kubectl scale deploy kafka-dummy-actor --replicas=7` to see the list fill in real-time and observe the actors moving around the map.