Description 
============



## Useful Commands


start Prometheus with:

```
docker-compose up -d
```

Restart:

```
curl -X POST http://localhost:9000/-/reload
```







## Test it

ab -n 10000 -c 100 http://localhost:80/endpoint1
ab -n 500 -c 100 http://localhost:80/endpoint2

Manually append lines to apache log (fluentd/grok_exporter will pick them up)

You can manually create a slow 1222ms response and a fast 33ms response:
```
$ docker exec -ti prometheus_spike_apache_1 bash

echo "172.18.0.1 - - [$(date "+%d/%b/%Y:%H:%M:%S %z")] \"GET /slowresponse HTTP/1.0\" 200 196 1222" >> logs/access_log
echo "172.18.0.1 - - [$(date "+%d/%b/%Y:%H:%M:%S %z")] \"GET /fastresponse HTTP/1.0\" 200 196 33" >> logs/access_log
```

NOTE: The above expression writes current timestamp with the unix date command:
```
date "+%d/%b/%Y:%H:%M:%S %z" #=> 11/Feb/2021:15:39:55 +0000
```

Test of the prometheus configuration:

```
go get -v github.com/prometheus/prometheus/cmd/promtool # <- takes forever

promtool check rules prometheus/alert.yml
```

## How to verify that alerts are triggered:

1. verify that metrics show your responses (in buckets corresponding the response time categories): http://localhost:9144/metrics

2. verify that alert triggers in Prometheus http://localhost:9000/new/alerts

3. verify that alert is sent from Prometheus to it's Alert manager: http://localhost:9093/#/alerts

4. verify that alert is written to file as Alert Manager sends to Fluentd:

```
$ docker exec -ti prometheus_spike_fluent_1 sh

tail -n 1 /tmp/alerts/alerts.log/*.log
2021-02-15T09:43:51+00:00	alert	{"receiver":"fluentdreciever","status":"firing","alerts":[{"status":"firing","labels":{"alertname":"InstanceDown","instance":"idonotexists:564","job":"services"},"annotations":{},"startsAt":"2021-02-15T08:35:16.877347671Z","endsAt":"0001-01-01T00:00:00Z","generatorURL":"http://686d2501c850:9090/graph?g0.expr=up%7Bjob%3D%22services%22%7D+%3C+1&g0.tab=1","fingerprint":"848d4fa77803ce9d"},{"status":"firing","labels":{"alertname":"SlowResponse2","severity":"critical"},"annotations":{"description":".....","summary":"Mere end 3 langsomme requests seneste time"},"startsAt":"2021-02-15T09:31:16.877347671Z","endsAt":"0001-01-01T00:00:00Z","generatorURL":"http://686d2501c850:9090/graph?g0.expr=sum%28floor%28increase%28http_latency_seconds_count%5B1h%5D%29%29%29+-+sum%28floor%28increase%28http_latency_seconds_bucket%7Ble%3D%221%22%7D%5B1h%5D%29%29%29+%3E%3D+3&g0.tab=1","fingerprint":"e4a26b1cdb7fcfe4"}],"groupLabels":{},"commonLabels":{},"commonAnnotations":{},"externalURL":"http://0531dc0b945f:9093","version":"4","groupKey":"{}:{}","truncatedAlerts":0}

```

NOTE: the alert is currently coded to trigger only if 3 slow responses are triggered within same hour

## inspirational links:

Inspired by https://github.com/magenta-aps/apache_log_exporter example of modified apache log to read stats. Then used first example from https://dev.to/ablx/minimal-prometheus-setup-with-docker-compose-56mp to setup prometheus for listening.