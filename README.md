# Konvoy + Kudo Studio

_NB: This is very much a work in progress. Suggestions, constructive criticism, and (especially) PRs are most welcome!_

Tested with Konvoy v1.0.0-rc.1 and Kudo v0.4.0 on AWS. 

![screencap-gif](https://github.com/tbaums/konvoy-kudo-studio/blob/master/2019_07_22-screencap.gif)


## Initial setup

### Deploy Kudo Kafka
1. `curl -O https://raw.githubusercontent.com/tbaums/konvoy-kudo-studio/master/install-kudo-prereqs.sh`
1. `sh install-kudo-prereqs.sh`
1. `kubectl kudo install zookeeper --instance=zk`
1. Wait for all 3 Zookeeper pods to be `RUNNING` and `READY`
1. `kubectl kudo install kafka --instance=kafka`

### Deploy Kafka Client API, Svelte front-end, and Dummy Actors
1. `kubectl apply -f https://raw.githubusercontent.com/tbaums/konvoy-kudo-studio/master/kafka-python-api/kafka-client-api.yaml`
1. `kubectl apply -f https://raw.githubusercontent.com/tbaums/konvoy-kudo-studio/master/svelte-ui/svelte-client.yaml`



### Navigate to Svelte UI
1. Visit \<your AWS elb\>/svelte

#### Manufacturing and IoT example
1. Click 'Manufactoring & IoT' in the Nav bar
1. Explain demo architecture
1. Click '-' button to collapse architecture diagram
1. Click button 'Click me to start fetch'
1. `kubectl apply -f https://raw.githubusercontent.com/tbaums/konvoy-kudo-studio/master/dummy-actors/kafka-dummy-actor.yaml`
1. Observe a single actor on the map (left) and in the actor list (on right).
1. Run `kubectl scale deploy kafka-dummy-actor --replicas=7` to see the list fill in real-time and observe the actors moving around the map.

#### User Research example

1. Click 'User Research' in the Nav bar
1. Explain demo architecture
1. Click '-' button to collapse architecture diagram
1. Open browser 'Network' panel
1. Move mouse across left-hand screenshot
1. Explain that each mouse movement captured by the browser is posted directly to the Python Kafka API server, via an endpoint exposed through Traefik
1. Observe Node.js Kafka API reading from Kafka queue and returning the mouse movements in the right-hand screenshot
1. Observe POST request duration (should be max 500ms)

#### Demonstrate the power of horizontal scaling
To demonstrate the power of granular microservice scaling, first we need to generate more load on the Python Kafka API. We will then observe POST request times increase. Lastly, we will scale the Python Kafka API and observe POST request times return to normal.

From User Research screen (assumes above demo steps completed):
1. `kubectl scale deploy kafka-dummy-actor --replicas=70`
1. Move mouse across left-hand panel
1. Observe POST request duration in browser's Network panel (should be >1000ms)
1. `kubectl scale deploy kafka-client-api --replicas=5`
1. Observe POST request duration (should return to ~250ms)
