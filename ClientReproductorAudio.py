
import paho.mqtt.client as mqtt #important el client
import pygame
import time
import threading

pygame.mixer.init()	
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)

DIFICULTAD=0 #variable dificultat, per defecte facil 0, 1 dificil

soundA1 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
soundA_1 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
soundB1 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
soundC1 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
soundC_1 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')

sound1A1 = pygame.mixer.Sound('/home/pi/audio2/A11.ogg')
sound3A1 = pygame.mixer.Sound('/home/pi/audio2/A13.ogg')

def comensa():
    #time.sleep(63)
    pygame.mixer.music.load('/home/pi/audio2/A11.ogg') #obrir eixe archiu
    pygame.mixer.music.play()
    pygame.mixer.music.load('/home/pi/audio2/A12.ogg')
    pygame.mixer.music.play(-1)

    #pygame.mixer.Sound.play(soundA1)
def finA():
    pygame.mixer.music.load('/home/pi/audio2/A13.ogg')
    pygame.mixer.music.play()

def comensa1():
    pygame.mixer.Sound.play(sound1A1)    
    pygame.mixer.music.load('/home/pi/audio2/A12.ogg')
    pygame.mixer.music.play(-1)

def finA1():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(sound3A1)
    


def on_message(client, userdata, message):    
    topic = str(message.topic)
    mes = str(message.payload.decode("utf-8"))
    print(topic+ " " + mes)
    
    if topic == "sala2/dificultad":
        if mes == "1":
            DIFICULTAD=1
    elif topic == "sala2/inici":
        hilo = threading.Thread(target=comensa)
        hilo.start()
    elif topic == "sala2/finA":
        hilo = threading.Thread(target=finA)
        hilo.start()

    elif topic == "sala2/inici1":
        hilo = threading.Thread(target=comensa1)
        hilo.start()
    elif topic == "sala2/finA1":
        hilo = threading.Thread(target=finA1)
        hilo.start()



    elif topic == "sala2/tecla1":
        time.sleep(1)
        pygame.mixer.Sound.play(soundB1)
    

def on_connect(client,userdata,flags,rc):
  
    client.subscribe("sala2/inici",1)
    client.subscribe("sala2/inici1",1)
    client.subscribe("sala2/finA",1)
    client.subscribe("sala2/finA1",1)

    for i in range(0,20):
        client.subscribe("sala2/tecla"+str(i),1)


    print("Suscrito a los temas tecla de 0 a 20")

broker_address="192.168.68.1" #ip del servidor
#broker_address="192.168.1.3"

print("Creando una estancia")
client = mqtt.Client("ReproductorAudio2") #creant una estancia
client.on_message=on_message #cridant a on_message
client.on_connect=on_connect #cridant a on_connect
print("Conectando con el servidor")
client.connect(broker_address) #conectant-se al servidor 
client.loop_forever()
