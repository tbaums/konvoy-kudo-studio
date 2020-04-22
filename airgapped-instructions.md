# Konvoy + Kudo Studio

## Airgapped environment instruction supplement

## Pull the following container images from DockerHub and push to local registry

1. tbaums/kafka-dummy-actor:latest
1. tbaums/kafka-node-js-api:latest
1. tbaums/svelte-client:latest
1. tbaums/kafka-client-api:latest
1. kudobuilder/controller:v0.12.0
1. zookeeper:3.4.14
1. quay.io/prometheus/node-exporter:v0.18.1
1. mesosphere/kafka:2.4.0-1.3.0


## Modify the YAML files below to point to your local images in your local registry
1. kafka-dummy-actors/kafka-dummy-actor.yaml
1. kafka-node-js-api/kafka-node-js-api.yaml
1. svelte-ui/svelte-client.yaml
1. kafka-python-api/kafka-client-api.yaml
1. Run `kubectl kudo init --dry-run -o yaml > kk-init.yaml` and edit the image in `kk-init.yaml`
1. Run `kubectl apply -f kk-init.yaml`
1. Edit `/zookeeper/templates/statefulset.yaml` to point to your local image of ZooKeeper.
1. FROM THE DIRECTORY WHERE THE ZOOKEEPER DIRECTORY SITS, run `kubectl kudo install zookeeper`.
1. Edit `/kafka/templates/statefulset.yaml` to point to your local image of `node-exporter:v0.18.1` and `kafka:2.4.0-1.3.0` 
1. FROM THE DIRECTORY WHERE THE ZOOKEEPER DIRECTORY SITS, run `kubectl kudo install kafka --instance=kafka -p ADD_SERVICE_MONITOR=true --wait`

Proceed to *Deploy Kafka Client API, Svelte front-end, and Node.js Websocket server* step in [main instructions](./README.md).
