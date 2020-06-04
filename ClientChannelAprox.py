
import paho.mqtt.client as mqtt #important el client
import pygame
import time
import subprocess
import threading

pygame.mixer.init()	
pygame.mixer.pre_init(frequency=44100, size=-16, channels=20, buffer=4096)
pygame.mixer.set_num_channels(20)

DIFICULTAD=0 #variable dificultat, per defecte facil 0, 1 dificil

tecla1_1 = pygame.mixer.Sound('/home/pi/audio2/A1c.wav')
#tecla1_2 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
#tecla1_3 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
tecla2_1 = pygame.mixer.Sound('/home/pi/audio2/A#1c.wav')
#tecla2_2 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla2_3 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
tecla3_1 = pygame.mixer.Sound('/home/pi/audio2/B1c.wav')
#tecla3_2 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla3_3 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
tecla4_1 = pygame.mixer.Sound('/home/pi/audio2/C1c.wav')
#tecla4_2 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla4_3 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
tecla5_1 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla5_2 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla5_3 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla6_1 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
tecla6_2 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
tecla6_3 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
tecla7_1 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
tecla7_2 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
tecla7_3 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
tecla8_1 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
tecla8_2 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
tecla8_3 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
tecla9_1 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
tecla9_2 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
tecla9_3 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
tecla10_1 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla10_2 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla10_3 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla11_1 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
tecla11_2 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
tecla11_3 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
tecla12_1 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
tecla12_2 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
tecla12_3 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
tecla13_1 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
tecla13_2 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
tecla13_3 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
tecla14_1 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
tecla14_2 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
tecla14_3 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
tecla15_1 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla15_2 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla15_3 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla16_1 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
tecla16_2 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
tecla16_3 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
tecla17_1 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
tecla17_2 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
tecla17_3 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
tecla18_1 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
tecla18_2 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
tecla18_3 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
tecla19_1 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
tecla19_2 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
tecla19_3 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
tecla20_1 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla20_2 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
tecla20_3 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')

#play()
#play a Sound on a specific Channel
#play(Sound, loops=0, maxtime=0, fade_ms=0) -> None

def tecla1_inici():    
    pygame.mixer.Channel(0).play(tecla1_1,-1,20000)

def tecla2_inici():
    pygame.mixer.Channel(1).play(tecla2_1,-1,20000)

def tecla3_inici():    
    pygame.mixer.Channel(2).play(tecla3_1,-1,20000)

def tecla4_inici():
    pygame.mixer.Channel(3).play(tecla4_1,-1,20000)

def on_message(client, userdata, message):    
    topic = str(message.topic)
    mes = str(message.payload.decode("utf-8"))
    print(topic+ " " + mes)
    
    if topic == "sala2/dificultad":
        if mes == "1":
            DIFICULTAD=1
    elif topic == "sala2/tecla1":
        print("ENTRA en tecla1")
        if mes == "1":
            print("ENTRA 1 en mes=1")
            if not pygame.mixer.Channel(0).get_busy():
                pygame.mixer.Channel(0).play(tecla1_1,-1,20000)
            #hilo = threading.Thread(target=tecla1_inici)
            #hilo.start()
        elif mes == "0":
            print("ENTRA 1 en mes=0")
            #fadeout() 
            # stop playback after fading channel out 
            # fadeout(time) -> None
            pygame.mixer.Channel(0).fadeout(200)
    elif topic == "sala2/tecla2":
        print("ENTRA en tecla2")
        if mes == "1":
            print("ENTRA 2 en mes=1")
            if not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(tecla2_1,-1,20000)
            #hilo = threading.Thread(target=tecla2_inici)
            #hilo.start()
        elif mes == "0":
            print("ENTRA 2 en mes=0")
            pygame.mixer.Channel(1).fadeout(200)
    elif topic == "sala2/tecla3":
        print("ENTRA en tecla3")
        if mes == "1":
            print("ENTRA 3 en mes=1")
            if not pygame.mixer.Channel(2).get_busy():
                pygame.mixer.Channel(2).play(tecla3_1,-1,20000)
            #hilo = threading.Thread(target=tecla3_inici)
            #hilo.start()
        elif mes == "0":
            print("ENTRA 3 en mes=0")
            pygame.mixer.Channel(2).fadeout(200)
    elif topic == "sala2/tecla4":
        print("ENTRA en tecla4")
        if mes == "1":
            print("ENTRA 4 en mes=1")
            if not pygame.mixer.Channel(3).get_busy():
                pygame.mixer.Channel(3).play(tecla4_1,-1,20000)
            #hilo = threading.Thread(target=tecla4_inici)
            #hilo.start()
        elif mes == "0":
            print("ENTRA 4 en mes=0")
            pygame.mixer.Channel(3).fadeout(200)
    elif topic == "sala2/tecla5":
        print("ENTRA en tecla5")
        if mes == "1":
            print("ENTRA 5 en mes=1")
            if not pygame.mixer.Channel(4).get_busy():
                pygame.mixer.Channel(4).play(tecla5_1,-1,20000)
            #hilo = threading.Thread(target=tecla1_inici)
            #hilo.start()
        elif mes == "0":
            print("ENTRA 5 en mes=0")
            #fadeout() 
            # stop playback after fading channel out 
            # fadeout(time) -> None
            pygame.mixer.Channel(4).fadeout(200)
    elif topic == "sala2/tecla6":
        print("ENTRA en tecla6")
        if mes == "1":
            print("ENTRA 6 en mes=1")
            if not pygame.mixer.Channel(5).get_busy():
                pygame.mixer.Channel(5).play(tecla6_1,-1,20000)
            #hilo = threading.Thread(target=tecla2_inici)
            #hilo.start()
        elif mes == "0":
            print("ENTRA 6 en mes=0")
            pygame.mixer.Channel(5).fadeout(200)
    elif topic == "sala2/tecla7":
        print("ENTRA en tecla7")
        if mes == "1":
            print("ENTRA 7 en mes=1")
            if not pygame.mixer.Channel(6).get_busy():
                pygame.mixer.Channel(6).play(tecla7_1,-1,20000)
            #hilo = threading.Thread(target=tecla3_inici)
            #hilo.start()
        elif mes == "0":
            print("ENTRA 7 en mes=0")
            pygame.mixer.Channel(6).fadeout(200)
    elif topic == "sala2/tecla8":
        print("ENTRA en tecla8")
        if mes == "1":
            print("ENTRA 8 en mes=1")
            if not pygame.mixer.Channel(7).get_busy():
                pygame.mixer.Channel(7).play(tecla8_1,-1,20000)
            #hilo = threading.Thread(target=tecla4_inici)
            #hilo.start()
        elif mes == "0":
            print("ENTRA 8 en mes=0")
            pygame.mixer.Channel(7).fadeout(200)
    
def on_connect(client,userdata,flags,rc):
  
    client.subscribe("sala2/dificultad",1)    

    for i in range(0,8):
        client.subscribe("sala2/tecla"+str(i),1)

    print("Suscrito a los temas tecla de 1 a 8")

broker_address="127.0.0.1" #ip del servidor
#broker_address="192.168.68.1" #ip del servidor
#broker_address="192.168.1.3"

print("Creando una estancia")
client = mqtt.Client("ReproductorAudio2") #creant una estancia
client.on_message=on_message #cridant a on_message
client.on_connect=on_connect #cridant a on_connect
print("Conectando con el servidor")
client.connect(broker_address) #conectant-se al servidor 
client.loop_forever()