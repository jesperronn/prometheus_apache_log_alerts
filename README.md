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

echo '172.18.0.1 - - [11/Feb/2021:15:39:55 +0000] "GET /slowresponse HTTP/1.0" 200 196 1222' >> logs/access_log
echo '172.18.0.1 - - [11/Feb/2021:15:39:55 +0000] "GET /fastresponse HTTP/1.0" 200 196 33' >> logs/access_log
```

Test of the prometheus configuration:

```
go get -v github.com/prometheus/prometheus/cmd/promtool # <- takes forever

promtool check rules prometheus/alert.yml
```


## inspirational links:

Inspired by https://github.com/magenta-aps/apache_log_exporter example of modified apache log to read stats. Then used first example from https://dev.to/ablx/minimal-prometheus-setup-with-docker-compose-56mp to setup prometheus for listening.