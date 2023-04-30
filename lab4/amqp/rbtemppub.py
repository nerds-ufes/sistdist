#!/usr/bin/env python
import pika
from pika.exchange_type import ExchangeType
import sys
from random import randrange, uniform
import time

# Calcula total de argumentos
n = len(sys.argv)
 
# Verificação do uso correto/argumentos
if (n!=3):
    print("\nUso correto: rbtemppub <broker_address> <group_id>.\n")
    exit(-1)

rabbitBroker = str(sys.argv[1])

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitBroker))

channel = connection.channel()
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

while True:
      message = str(uniform(15, 40))
      topic = "sd/" + str(sys.argv[2]) + "/temp"
      channel.basic_publish(exchange='', routing_key=topic, body=message)
      print("Sent " + message + "to topic " + topic)
      time.sleep(1)

connection.close()

