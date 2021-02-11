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







Test it:

ab -n 10000 -c 100 http://localhost:80/endpoint1
ab -n 500 -c 100 http://localhost:80/endpoint2



Test configuration:

go get -v github.com/prometheus/prometheus/cmd/promtool # <- takes forever

promtool check rules prometheus/alert.yml


inspirational links:

Inspired by https://github.com/magenta-aps/apache_log_exporter example of modified apache log to read stats. Then used first example from https://dev.to/ablx/minimal-prometheus-setup-with-docker-compose-56mp to setup prometheus for listening.