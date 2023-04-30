#!/usr/bin/env python
import pika
from pika.exchange_type import ExchangeType
import sys
from random import randrange, uniform
import time
import os
import json

def main():
    # Calcula total de argumentos
    n = len(sys.argv)
 
    # Verificação do uso correto/argumentos
    if (n!=3):
       print("\nUso correto: rbtempsub <broker_address> <group_id>.\n")
       exit(-1)

    rabbitBroker = str(sys.argv[1])
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitBroker))
    channel = connection.channel()

    topic = "sd/" + str(sys.argv[2]) + "/temp"
    
    channel.queue_declare(queue=topic)

    def callback(ch, method, properties, body):
        print("Received " + str(json.loads(body)))

    channel.basic_consume(queue=topic, on_message_callback=callback, auto_ack=True)

    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
