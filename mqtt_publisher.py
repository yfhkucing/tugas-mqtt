import random
import time
from paho.mqtt import client as mqtt_client
import serial
from datetime import datetime
arduino_port = "/dev/ttyACM0" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
ser = serial.Serial(arduino_port, baud)
broker = 'broker.emqx.io'
port = 1883
topic = "psi/postes"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
            client = mqtt_client.Client(client_id)
            client.on_connect = on_connect
            client.connect(broker, port)
            return client

def publish(client):
    while True:
        time.sleep(1)
        getData=str(ser.readline(),"utf-8")
        msg = f"messages: {getData}"
        result = client.publish(topic, msg)
    # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
            
def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
