#!/usr/bin/python
import subprocess
import time
import threading
import paho.mqtt.client as mqtt
import os

#Evita que la pantalla se apague
os.system("xset -dpms")
os.system("xset s noblank")
os.system("xset s off")
def holograma1():
    subprocess.call(['cvlc','--x11-display',':0','-f','--no-video-title','--play-and-exit','--no-one-instance','--video-on-top','/home/pi/holograma1.mp4'])

def holograma2():
    subprocess.call(['cvlc','--x11-display',':0','-f','--no-video-title','--play-and-exit','--no-one-instance','--video-on-top','/home/pi/holograma2.mp4'])

def conexio():
    subprocess.call(['chromium-browser','-noerrdialogs','--disable-session-crashed-bubble','--start-fullscreen','http://192.168.69.47:8080'])

def apaga():
    subprocess.call(['killall','vlc'])

def on_connect(client,userdata,flags,rc):
    client.subscribe("sala2/holograma1")
    client.subscribe("sala2/holograma2")
    client.subscribe("sala2/audioHolograma")
    client.subscribe("sala2/holograma")
    client.subscribe("sala2/desactivaHolograma")

def on_message(client,userdata,message):

    mes = str(message.payload.decode("utf-8"))
    topic = str(message.topic.decode("utf-8"))
    print(topic)

    if topic == "sala2/holograma1":
        hilo = threading.Thread(target=holograma1)
        hilo.start()
    elif topic == "sala2/holograma2":
        hilo = threading.Thread(target=holograma2)
        hilo.start()
    elif topic == "sala2/audioHolograma":
	hilo = threading.Thread(target=conexio)
	hilo.start()
    elif topic == "sala2/holograma":
        hilo = threading.Thread(target=holograma1)
        hilo.start()
    elif topic == "sala2/desactivaHolograma":
        hilo = threading.Thread(target=apaga)
        hilo.start()

#broker_address="192.168.1.8"
broker_address="192.168.68.55"

print("Creando una instancia cliente")
client = mqtt.Client("Holograma")
client.on_message=on_message
client.on_connect=on_connect

client.connect(broker_address)

client.loop_forever()
