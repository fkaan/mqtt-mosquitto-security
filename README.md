# mqtt-mosquitto-security(for windows)
Step-by-step guide and scripts for setting up TLS/SSL certificates for MQTT Mosquitto broker. Implementing username and password authentication for MQTT clients using Mosquitto.
# MQTT Mosquitto Secure Setup and Authentication
(You should write the following codes in windows command line)
## TLS/SSL Certificate Setup:
Generate CA Key and Certificate:
```python
openssl genrsa -des3 -out ca.key 2048
openssl req -new -x509 -days 1826 -key ca.key -out ca.crt
```
Generate Server Key and Certificate:
```python
openssl genrsa -out server.key 2048
openssl req -new -out server.csr -key server.key
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 360
```
Securely Subscribe to a Topic:
```python
mosquitto_sub -h "your broker ip" -p 8883 -t test --cafile "C:\Program Files\mosquitto\certs\ca.crt" --tls-version tlsv1.2
```
Securely Publish a Message:
```python
mosquitto_pub -h "your broker ip" -p 8883 -t test --cafile "C:\Program Files\mosquitto\certs\ca.crt" --tls-version tlsv1.2 -d
```
# Client Key Setup:
## Generate Client Key and Certificate:
```python
openssl genrsa -out client.key 2048
openssl req -new -out client.csr -key client.key
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 360
```
## Securely Publish with Client Credentials:
```python
mosquitto_pub --cafile "C:\Program Files\mosquitto\certs\ca.crt" --cert "C:\Program Files\mosquitto\certs\client.crt" --key "C:\Program Files\mosquitto\certs\client.key" -d -h fekef -p 8883 -t test -m "hello world"
```
## Username and Password Authentication:
Generate Username and Password:
First, you must create password folder in C:\Program Files\mosquitto\ then create password.txt.
```python
mosquitto_passwd -c "C:\Program Files\mosquitto\passwords\password.txt" root #Root is the name of user you can do what you want
mosquitto_passwd -D "C:\Program Files\mosquitto\passwords\password.txt" root #To delete a user
```

## Add following lines to bottom of /mosquitto/mosquitto.conf or create new .conf file.
```python
listener 8883
per_listener_settings true

password_file  C:\Program Files\mosquitto\passwords\password.txt
allow_anonymous false 
protocol mqtt

cafile C:\Program Files\mosquitto\certs\ca.crt
certfile C:\Program Files\mosquitto\certs\server.crt
keyfile C:\Program Files\mosquitto\certs\server.key

tls_version tlsv1.2
```
## After updating mosquitto.conf, start the mosquitto server
```python
mosquitto -c mosquitto.conf -v
```
# Resources
[MQTT](https://mqtt.org)
[MOSQUITTO](https://mosquitto.org)
[OPENSSL](https://pypi.org/project/pyOpenSSL/)
