register-postgres:
	curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @register-postgres.json

create-consumer:
	docker-compose -f docker-compose.yml exec kafka /kafka/bin/kafka-console-consumer.sh \
    --bootstrap-server kafka:9092 \
    --from-beginning \
    --property print.key=true \
    --topic dbserver1.inventory.customers

get-jupyter-token:
	docker-compose -f docker-compose.yml exec jupyter-local jupyter notebook list

get-postgres-driver:
	docker-compose -f docker-compose.yml exec jupyter-local \
	wget -P /home/jovyan https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.5/postgresql-42.2.5.jar
