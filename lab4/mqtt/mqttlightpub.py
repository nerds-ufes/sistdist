import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import sys

# Calcula total de argumentos
n = len(sys.argv)
 
# Verificação do uso correto/argumentos
if (n!=3):
    print("\nUso correto: mqttlightpub <broker_address> <group_id>.\n")
    exit(-1)

mqttBroker = str(sys.argv[1])
#mqttBroker = "broker.emqx.io" 

client = mqtt.Client("LightPub-" + str(sys.argv[2]))
client.connect(mqttBroker) 

while True:
    randNumber = uniform(0, 100)
    topic = "sd/" + str(sys.argv[2]) + "/light"
    client.publish(topic, randNumber)
    print("Published " + str(randNumber) + " to topic " + topic)
    time.sleep(1)

