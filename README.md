# Postgres CDC example

This is a very simple example of PostgreSQL CDC via amazing Debezium Connector.

## Commands reference:

- first of all, run:
```
docker-compose up --build
```
- to get the jupyter token, please run:
```
docker-compose -f docker-compose.yml exec jupyter-local jupyter notebook list
```
In answer you will receive:
```
Currently running servers:
http://0.0.0.0:8888/?token={here goes your token} :: /home/jovyan
```
Please copy the provided link to the browser.


## Data Schema
- Customers:
```
Column      |          Type          |                       Modifiers
------------+------------------------+--------------------------------------------------------
id          | integer                | not null default nextval('customers_id_seq'::regclass)
first_name  | character varying(255) | not null
last_name   | character varying(255) | not null
email       | character varying(255) | not null
```
- Orders
```
Column      |  Type   |                      Modifiers
------------+---------+-----------------------------------------------------
id          | integer | not null default nextval('orders_id_seq'::regclass)
order_date  | date    | not null
purchaser   | integer | not null
quantity    | integer | not null
product_id  | integer | not null
```
- Products
```
Column       |          Type          |                       Modifiers
-------------+------------------------+-------------------------------------------------------
id           | integer                | not null default nextval('products_id_seq'::regclass)
name         | character varying(255) | not null
description  | character varying(512) |
weight       | double precision       |
```
- Products on hand:
```
Column      |  Type   | Modifiers
------------+---------+-----------
product_id  | integer | not null
quantity    | integer | not null
```

## Misc
To connect to the database directly, please use:
```
docker-compose  \
  -f docker-compose.yml \
  exec postgres env PGOPTIONS="--search_path=inventory" \
  bash -c 'psql -U $POSTGRES_USER postgres'
```
