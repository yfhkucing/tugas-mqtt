import random
from paho.mqtt import client as mqtt_client
import time
broker = 'broker.emqx.io'
port = 1883
topic = "psi/postes"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
            client = mqtt_client.Client(client_id)
            client.on_connect = on_connect
            client.connect(broker, port)
            return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        mes=msg.payload.decode()
        split=mes.split(",")
        CO=float(split[0])
        Temp=float(split[1])
        ph=float(split[2])
        Amon=float(split[3])
        oksi=float(split[4])
        print("\n-------------")
        print("CO2 = %.2f"%CO)
        if CO>1000:
            print('Kadar CO2 Terlalu Tinggi\n')
        elif CO<=1000 :
            print('Kadar CO2 Normal\n')
            print("Temperatur = %.2f"%Temp)
        if Temp>25:
            print('Temperatur Terlalu Tinggi\n')
        elif Temp<20:
            print('Temperatur Terlalu Rendah\n')
        elif Temp>=20 and Temp<=25 :
            print('Temperatur Normal\n')
            print("PH = %.2f"%ph)
        if ph>8:
            print('PH Terlalu Tinggi\n')
        elif Temp<6.5:
            print('PH Terlalu Rendah\n')
        else:
            print('PH Normal\n')
            print("Amonia = %.2f"%Amon)
        if Amon>0.02:
            print('Kadar Amonia Terlalu Tinggi\n')
        elif Amon<=0.02 :
            print('Kadar Amonia Normal\n')
            print("Oksigen = %.2f"%oksi)
        if oksi>=5:
            print('Kadar Oksigen Normal\n')
        elif oksi<5 :
            print('Kadar Oksigen Terlalu Rendah\n')
            print("-------------\n")
            time.sleep(1)
            client.subscribe(topic)
            client.on_message = on_message
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
if __name__ == '__main__':
 run()