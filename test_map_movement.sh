#!/bin/bash
function send() {
    x=$1
    y=$2

curl  -X POST \
  "http://ad51b5465a4a011e987c20aaf9c2019a-392664409.us-west-2.elb.amazonaws.com/kafka-client-api/write?topic=topic2-2&payload={'actor':'actor1','x':$x,'y':$y}&repetitions=1" \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: ad51b5465a4a011e987c20aaf9c2019a-392664409.us-west-2.elb.amazonaws.com' \
  -H 'Postman-Token: 3eb1e067-d0f6-4eda-8e09-136dc8a00960,791e7f51-5f28-44c3-9d6e-49cd1688d018' \
  -H 'User-Agent: PostmanRuntime/7.15.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'content-length: ' \
  -H 'referer: http://ad51b5465a4a011e987c20aaf9c2019a-392664409.us-west-2.elb.amazonaws.com/kafka-client-api/write?topic=topic2-2&payload=%7B%22actor%22:%22actor1%22,%20%22x%22:%20%2220%22,%20%22y%22:%2250%22%7D&repetitions=1' 
   
}

for i in {1..3}
do
    send $i $i
    sleep .5
done