import sys
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message on " + str(message.topic) + ": " + str(message.payload.decode("utf-8")))

# Calcula total de argumentos
n = len(sys.argv)
 
# Verificação do uso correto/argumentos
if (n!=3):
    print("\nUso correto: mqtttempsub <broker_address> <group_id>.\n")
    exit(-1)

mqttBroker = str(sys.argv[1])
#mqttBroker = "broker.emqx.io" 

client = mqtt.Client("TempSub-" + str(sys.argv[2]))
client.connect(mqttBroker) 

client.loop_start()

topic = "sd/" + str(sys.argv[2]) + "/temp"
client.subscribe(topic)
    
client.on_message=on_message 
time.sleep(30000)
client.loop_stop()

