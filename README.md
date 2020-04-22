# Konvoy + Kudo Studio

_NB: Suggestions, constructive criticism, and (especially) PRs are most welcome!_

Tested on AWS and Azure with:
- Konvoy v1.4.2
- KUDO v0.12.0
- Kafka Operator Version v1.2.0
- Zookeeper Operator Version v0.3.0

![screencap-gif](https://github.com/tbaums/konvoy-kudo-studio/blob/master/2019_07_22-screencap.gif)

## Prerequisites

1. This demo assumes you have `kubectl` installed and connected to a Konvoy cluster.  
2. Install the KUDO CLI plugin for `kubectl` via: `brew install kudo-cli` / `brew upgrade kudo-cli` OR `kubectl krew install kudo` / `kubectl krew upgrade kudo`
1. Confirm you are running the latest KUDO CLI (v0.12.0) via: `kubectl kudo --version`
1. To execute in an airgapped environment, please follow the [airgapped instructions](./airgapped-instructions.md) before proceeding.

## Initial setup

### Import Kafka dashboard

1. Nagivate to Grafana
1. Hover over `+` in left-hand side nav bar
1. Select import
1. Copy and paste JSON found [here](https://raw.githubusercontent.com/kudobuilder/operators/master/repository/kafka/docs/latest/resources/grafana-dashboard.json)
1. Click `Upload`
1. Select `Prometheus` as data source

### Deploy Kudo Kafka

1. Confirm you do not have an earlier version of KUDO deployed to your cluster by running `kubectl get ns kudo-system`. If kubectl responds saying the namespace was not found, proceed to the next step. If you discover that KUDO is already installed in your cluster, please begin by deleting the KUDO instance on your cluster: `kubectl kudo init --dry-run -o yaml | kubectl delete -f -`
1. Install KUDO on your cluster: `kubectl kudo init --wait`
1. Next, install Zookeeper, which is a dependency for Kafka: `kubectl kudo install zookeeper --wait`
1. Wait for all 3 Zookeeper pods to be `RUNNING` and `READY`
1. `kubectl kudo install kafka --instance=kafka -p ADD_SERVICE_MONITOR=true --wait`
1. Wait for all 3 Kafka brokers to be `RUNNING` and `READY`

### Deploy Kafka Client API, Svelte front-end, and Node.js Websocket server
1. `kubectl apply -f https://raw.githubusercontent.com/tbaums/konvoy-kudo-studio/master/kafka-client-api/kafka-client-api.yaml`
1. `kubectl apply -f https://raw.githubusercontent.com/tbaums/konvoy-kudo-studio/master/svelte-ui/svelte-client.yaml`
1. `kubectl apply -f https://raw.githubusercontent.com/tbaums/konvoy-kudo-studio/master/kafka-node-js-api/kafka-node-js-api.yaml`
1. `kubectl apply -f https://raw.githubusercontent.com/tbaums/konvoy-kudo-studio/master/kafka-dummy-actors/kafka-dummy-actor.yaml`



### Navigate to Svelte UI
1. Visit \<your AWS elb\>/svelte

### Begin demonstration

#### Manufacturing and IoT example
1. Click 'Manufactoring & IoT' in the Nav bar
1. Explain demo architecture
1. Click '-' button to collapse architecture diagram
1. Click button 'Click me to start fetch'
1. Run `kubectl scale deploy kafka-dummy-actor --replicas=1`
1. Observe a single actor on the map (left) and in the actor list (on right).
1. Run `kubectl scale deploy kafka-dummy-actor --replicas=7` to see the list fill in real-time and observe the actors moving around the map.

#### User Research example

1. Click 'User Research' in the Nav bar
1. Explain demo architecture
1. Click '-' button to collapse architecture diagram
1. Open browser 'Network' panel and reload the page. (Right click on the page, and select "Inspect Element". Then, select the 'Network' panel tab. Reload the page to start capturing network traffic.)
1. Move mouse across left-hand screenshot
1. Explain that each mouse movement captured by the browser is posted directly to the Python Kafka API server, via an endpoint exposed through Traefik
1. Observe Node.js Kafka API reading from Kafka queue and returning the mouse movements in the right-hand screenshot
1. Observe POST request duration (should be ~500ms)

#### Demonstrate the power of horizontal scaling
To demonstrate the power of granular microservice scaling, first we need to generate more load on the Python Kafka API. We will then observe POST request times increase. Lastly, we will scale the Python Kafka API and observe POST request times return to normal.

From User Research screen (assumes above demo steps completed):
1. `kubectl scale deploy kafka-dummy-actor --replicas=70`
1. Move mouse across left-hand panel
1. Observe POST request duration in browser's Network panel (should be >1000ms)
1. `kubectl scale deploy kafka-client-api --replicas=5`
1. Observe POST request duration (should return to ~500ms)

#### 
