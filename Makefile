register-postgres:
	curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @register-postgres.json

create-consumer:
	docker-compose -f docker-compose.yml exec kafka /kafka/bin/kafka-console-consumer.sh \
    --bootstrap-server kafka:9092 \
    --from-beginning \
    --property print.key=true \
		--property print.value=false \
    --topic dbserver1.inventory.customers

get-jupyter-token:
	docker-compose -f docker-compose.yml exec jupyter-local jupyter notebook list

run-streamer:
	docker-compose  \
	-f docker-compose.yml exec jupyter-local /usr/local/spark/bin/spark-submit \
	--packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.3 \
	/home/jovyan/work/cdc_reader.py
