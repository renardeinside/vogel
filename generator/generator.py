import psycopg2

def connect_to_postgres():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        host="postgres",
        password="postgres",
        port=5432,
        options=f'-c search_path=inventory')
    return conn

connection = connect_to_postgres()
cursor = connection.cursor()
connection.commit()

from faker import Faker
fake = Faker()

def insert_new_customer(connection, cursor):
    cursor.execute("INSERT INTO customers (first_name, last_name, email) VALUES(%s, %s, %s)", (fake.first_name(),fake.last_name(),fake.email()))
    print("Inserting new customer")
    connection.commit()

def update_old_customer(connection, cursor):
    cursor.execute("select id from customers ORDER BY random()")
    customer_id = cursor.fetchone()[0]
    cursor.execute("UPDATE customers SET email = %s where id = %s", (fake.email(),customer_id))
    print("Updating old customer with id = %s" % customer_id)
    connection.commit()

def delete_customer(connection, cursor):
    cursor.execute("select id from customers where id>1004 ORDER BY random()")
    customer_id = cursor.fetchone()[0]
    cursor.execute("DELETE FROM customers where id = %s", (customer_id,))
    print("Deleting customer with id = %s" % customer_id  )
    connection.commit()


insert_new_customer(connection, cursor)
insert_new_customer(connection, cursor)
update_old_customer(connection, cursor)
delete_customer(connection, cursor)


import random

def generate_operation():
    randomizer = random.random()
    if randomizer>0.9:
        delete_customer(connection, cursor)
    elif (randomizer>0.7 and randomizer<=0.9):
        update_old_customer(connection, cursor)
    else:
        insert_new_customer(connection, cursor)

import time

ops_counter = 0

time.sleep(20) # wait for postgres

while True:
    generate_operation()
    ops_counter = ops_counter + 1
    time.sleep(3)
    if ops_counter % 10 == 0:
        time.sleep(10)
