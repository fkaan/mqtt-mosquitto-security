import paho.mqtt.client as mqtt
import time
import config

broker = "broker ip/address"
def on_connect(client, userdata, flags, rc):
    print("Connected ", rc)

client = mqtt.Client()
client.username_pw_set("username", "password")#username and password
client.tls_set('server_certificate','client_certificate','client_key')
client.tls_insecure_set(True)

client.connect(broker, 8883)
client.loop_start()

while True:
    message = input("Enter a message: ")
    if message == 'q':
        break
    client.publish("test/topic", message, qos= 1)#topic must to be same with subs topic

time.sleep(5)
client.loop_stop()
client.disconnect()
