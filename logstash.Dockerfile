FROM  docker.elastic.co/logstash/logstash:7.11.1

# for debug.level and logs path if needed
COPY config/logstash.yml /usr/share/logstash/config/logstash.yml

# not needed for now
# COPY log4j2.properties ../config/logstash_log4j2.properties

COPY config/logstash_pipeline.conf /usr/share/logstash/pipeline/logstash.conf