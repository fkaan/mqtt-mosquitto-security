import paho.mqtt.client as mqtt
import time 
import config

broker = "broker ip/address"
def on_connect(client, userdata, flags, rc):
    print("Connected : ", rc)
    client.subscribe("test/topic", qos = 1)

def on_message(client, userdata, message):
    print("Mesaj : ", message.payload.decode())

client = mqtt.Client()
client.username_pw_set("username", "password")#username and password
client.tls_set('server_certificate','client_certificate','client_key')
client.tls_insecure_set(True)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 8883)
client.loop_forever()
