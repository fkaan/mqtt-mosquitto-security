# mqtt-mosquitto-security
Step-by-step guide and scripts for setting up TLS/SSL certificates for MQTT Mosquitto broker. Implementing username and password authentication for MQTT clients using Mosquitto.
# MQTT Mosquitto Secure Setup and Authentication
TLS/SSL Certificate Setup:
Generate CA Key and Certificate:

openssl genrsa -des3 -out ca.key 2048
openssl req -new -x509 -days 1826 -key ca.key -out ca.crt
Generate Server Key and Certificate:

openssl genrsa -out server.key 2048
openssl req -new -out server.csr -key server.key
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 360
Securely Subscribe to a Topic:

mosquitto_sub -h 192.168.68.131 -p 8883 -t test --cafile "C:\Program Files\mosquitto\certs\ca.crt" --tls-version tlsv1.2
Securely Publish a Message:

mosquitto_pub -h 192.168.68.131 -p 8883 -t test --cafile "C:\Program Files\mosquitto\certs\ca.crt" --tls-version tlsv1.2 -d
