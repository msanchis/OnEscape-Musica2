import paho.mqtt.client as mqtt #important el client
import pygame
import time
import subprocess
import threading

pygame.mixer.init()	
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)

tecla2=False

tecla2_1 = pygame.mixer.Sound('/home/pi/audio2/B1-1.ogg')
tecla2_2 = pygame.mixer.Sound('/home/pi/audio2/B1-2.ogg')
tecla2_3 = pygame.mixer.Sound('/home/pi/audio2/B1-3.ogg')

def tecla2_inici():
    global tecla2
    tecla2=True
    pygame.mixer.Sound.play(tecla2_1)
    while(tecla2):
        pygame.mixer.Sound.play(tecla2_2)
    #pygame.mixer.Sound.play(tecla2_3) 

def on_message(client, userdata, message):    
    topic = str(message.topic)
    mes = str(message.payload.decode("utf-8"))
    print(topic+ " " + mes)
    if topic == "sala2/tecla3":
        print("ENTRA en tecla3")
        if mes == "1":
            print("ENTRA 3 en mes=1")
            hilo = threading.Thread(target=tecla2_inici)
            hilo.start()
        elif mes == "0":
            print("ENTRA 3 en mes=0")
            pygame.mixer.Sound.fadeout()
            global tecla2
            tecla2=False
        
def on_connect(client,userdata,flags,rc):
  
    client.subscribe("sala2/dificultad",1)    
    client.subscribe("sala2/tecla3",1)
    print("Suscrito a los temas dificultad y tecla3")

broker_address="127.0.0.1" #ip del servidor
#broker_address="192.168.68.1" #ip del servidor
#broker_address="192.168.1.3"

print("Creando una estancia")
client = mqtt.Client("ProvaTecla3") #creant una estancia
client.on_message=on_message #cridant a on_message
client.on_connect=on_connect #cridant a on_connect
print("Conectando con el servidor")
client.connect(broker_address) #conectant-se al servidor 
client.loop_forever()
