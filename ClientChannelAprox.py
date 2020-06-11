
import paho.mqtt.client as mqtt #important el client
import pygame
import time
import subprocess
import threading

pygame.mixer.init()	
pygame.mixer.pre_init(frequency=44100, size=-16, channels=20, buffer=4096)
pygame.mixer.set_num_channels(20)

DIFICULTAD=0 #variable dificultat, per defecte facil 0, 1 dificil

tecla1_1 = pygame.mixer.Sound('/home/pi/audio2/A#1.ogg')
tecla2_1 = pygame.mixer.Sound('/home/pi/audio2/C#1.ogg')
tecla3_1 = pygame.mixer.Sound('/home/pi/audio2/C#2.ogg')
tecla4_1 = pygame.mixer.Sound('/home/pi/audio2/D#1.ogg')
tecla5_1 = pygame.mixer.Sound('/home/pi/audio2/D#2.ogg')
tecla6_1 = pygame.mixer.Sound('/home/pi/audio2/F#1.ogg')
tecla7_1 = pygame.mixer.Sound('/home/pi/audio2/F#2.ogg')
tecla8_1 = pygame.mixer.Sound('/home/pi/audio2/G#1.ogg')
tecla9_1 = pygame.mixer.Sound('/home/pi/audio2/A1.ogg')
tecla10_1 = pygame.mixer.Sound('/home/pi/audio2/B1.ogg')
tecla11_1 = pygame.mixer.Sound('/home/pi/audio2/C1.ogg')
tecla12_1 = pygame.mixer.Sound('/home/pi/audio2/C2.ogg')
tecla13_1 = pygame.mixer.Sound('/home/pi/audio2/D1.ogg')
tecla14_1 = pygame.mixer.Sound('/home/pi/audio2/D2.ogg')
tecla15_1 = pygame.mixer.Sound('/home/pi/audio2/E1.ogg')
tecla16_1 = pygame.mixer.Sound('/home/pi/audio2/E2.ogg')
tecla17_1 = pygame.mixer.Sound('/home/pi/audio2/F1.ogg')
tecla18_1 = pygame.mixer.Sound('/home/pi/audio2/F2.ogg')
tecla19_1 = pygame.mixer.Sound('/home/pi/audio2/G1.ogg')
tecla20_1 = pygame.mixer.Sound('/home/pi/audio2/G2.ogg')

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
        elif mes == "0":
            print("ENTRA 2 en mes=0")
            pygame.mixer.Channel(1).fadeout(200)
    elif topic == "sala2/tecla3":
        print("ENTRA en tecla3")
        if mes == "1":
            print("ENTRA 3 en mes=1")
            if not pygame.mixer.Channel(2).get_busy():
                pygame.mixer.Channel(2).play(tecla3_1,-1,20000)            
        elif mes == "0":
            print("ENTRA 3 en mes=0")
            pygame.mixer.Channel(2).fadeout(200)
    elif topic == "sala2/tecla4":
        print("ENTRA en tecla4")
        if mes == "1":
            print("ENTRA 4 en mes=1")
            if not pygame.mixer.Channel(3).get_busy():
                pygame.mixer.Channel(3).play(tecla4_1,-1,20000)            
        elif mes == "0":
            print("ENTRA 4 en mes=0")
            pygame.mixer.Channel(3).fadeout(200)
    elif topic == "sala2/tecla5":
        print("ENTRA en tecla5")
        if mes == "1":
            print("ENTRA 5 en mes=1")
            if not pygame.mixer.Channel(4).get_busy():
                pygame.mixer.Channel(4).play(tecla5_1,-1,20000)
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
        elif mes == "0":
            print("ENTRA 6 en mes=0")
            pygame.mixer.Channel(5).fadeout(200)
    elif topic == "sala2/tecla7":
        print("ENTRA en tecla7")
        if mes == "1":
            print("ENTRA 7 en mes=1")
            if not pygame.mixer.Channel(6).get_busy():
                pygame.mixer.Channel(6).play(tecla7_1,-1,20000)            
        elif mes == "0":
            print("ENTRA 7 en mes=0")
            pygame.mixer.Channel(6).fadeout(200)
    elif topic == "sala2/tecla8":
        print("ENTRA en tecla8")
        if mes == "1":
            print("ENTRA 8 en mes=1")
            if not pygame.mixer.Channel(7).get_busy():
                pygame.mixer.Channel(7).play(tecla8_1,-1,20000)            
        elif mes == "0":
            print("ENTRA 8 en mes=0")
            pygame.mixer.Channel(7).fadeout(200)
    elif topic == "sala2/tecla9":
        print("ENTRA en tecla9")
        if mes == "1":
            print("ENTRA 9 en mes=1")
            if not pygame.mixer.Channel(8).get_busy():
                pygame.mixer.Channel(8).play(tecla9_1,-1,20000)
            
        elif mes == "0":
            print("ENTRA 9 en mes=0")
            #fadeout() 
            # stop playback after fading channel out 
            # fadeout(time) -> None
            pygame.mixer.Channel(8).fadeout(200)
    elif topic == "sala2/tecla10":
        print("ENTRA en tecla10")
        if mes == "1":
            print("ENTRA 10 en mes=1")
            if not pygame.mixer.Channel(9).get_busy():
                pygame.mixer.Channel(9).play(tecla10_1,-1,20000)            
        elif mes == "0":
            print("ENTRA 10 en mes=0")
            pygame.mixer.Channel(9).fadeout(200)
    elif topic == "sala2/tecla11":
        print("ENTRA en tecla11")
        if mes == "1":
            print("ENTRA 11 en mes=1")
            if not pygame.mixer.Channel(10).get_busy():
                pygame.mixer.Channel(10).play(tecla11_1,-1,20000)            
        elif mes == "0":
            print("ENTRA 11 en mes=0")
            pygame.mixer.Channel(10).fadeout(200)
    elif topic == "sala2/tecla12":
        print("ENTRA en tecla12")
        if mes == "1":
            print("ENTRA 12 en mes=1")
            if not pygame.mixer.Channel(11).get_busy():
                pygame.mixer.Channel(11).play(tecla12_1,-1,20000)
        elif mes == "0":
            print("ENTRA 12 en mes=0")
            pygame.mixer.Channel(11).fadeout(200)
    elif topic == "sala2/tecla13":
        print("ENTRA en tecla13")
        if mes == "1":
            print("ENTRA 13 en mes=1")
            if not pygame.mixer.Channel(12).get_busy():
                pygame.mixer.Channel(12).play(tecla13_1,-1,20000)
        elif mes == "0":
            print("ENTRA 13 en mes=0")
            #fadeout() 
            # stop playback after fading channel out 
            # fadeout(time) -> None
            pygame.mixer.Channel(12).fadeout(200)
    elif topic == "sala2/tecla14":
        print("ENTRA en tecla14")
        if mes == "1":
            print("ENTRA 14 en mes=1")
            if not pygame.mixer.Channel(13).get_busy():
                pygame.mixer.Channel(13).play(tecla14_1,-1,20000)            
        elif mes == "0":
            print("ENTRA 14 en mes=0")
            pygame.mixer.Channel(13).fadeout(200)
    elif topic == "sala2/tecla15":
        print("ENTRA en tecla15")
        if mes == "1":
            print("ENTRA 15 en mes=1")
            if not pygame.mixer.Channel(14).get_busy():
                pygame.mixer.Channel(14).play(tecla15_1,-1,20000)
        elif mes == "0":
            print("ENTRA 15 en mes=0")
            pygame.mixer.Channel(14).fadeout(200)
    elif topic == "sala2/tecla16":
        print("ENTRA en tecla16")
        if mes == "1":
            print("ENTRA 16 en mes=1")
            if not pygame.mixer.Channel(15).get_busy():
                pygame.mixer.Channel(15).play(tecla16_1,-1,20000)
        elif mes == "0":
            print("ENTRA 16 en mes=0")
            pygame.mixer.Channel(15).fadeout(200)
    elif topic == "sala2/tecla17":
        print("ENTRA en tecla17")
        if mes == "1":
            print("ENTRA 17 en mes=1")
            if not pygame.mixer.Channel(16).get_busy():
                pygame.mixer.Channel(16).play(tecla17_1,-1,20000)
        elif mes == "0":
            print("ENTRA 17 en mes=0")
            #fadeout() 
            # stop playback after fading channel out 
            # fadeout(time) -> None
            pygame.mixer.Channel(16).fadeout(200)
    elif topic == "sala2/tecla18":
        print("ENTRA en tecla18")
        if mes == "1":
            print("ENTRA 18 en mes=1")
            if not pygame.mixer.Channel(17).get_busy():
                pygame.mixer.Channel(17).play(tecla18_1,-1,20000)            
        elif mes == "0":
            print("ENTRA 18 en mes=0")
            pygame.mixer.Channel(17).fadeout(200)
    elif topic == "sala2/tecla19":
        print("ENTRA en tecla19")
        if mes == "1":
            print("ENTRA 19 en mes=1")
            if not pygame.mixer.Channel(18).get_busy():
                pygame.mixer.Channel(18).play(tecla19_1,-1,20000)
        elif mes == "0":
            print("ENTRA 19 en mes=0")
            pygame.mixer.Channel(18).fadeout(200)
    elif topic == "sala2/tecla20":
        print("ENTRA en tecla20")
        if mes == "1":
            print("ENTRA 20 en mes=1")
            if not pygame.mixer.Channel(19).get_busy():
                pygame.mixer.Channel(19).play(tecla20_1,-1,20000)
        elif mes == "0":
            print("ENTRA 20 en mes=0")
            pygame.mixer.Channel(19).fadeout(200)

def on_connect(client,userdata,flags,rc):
  
    client.subscribe("sala2/dificultad",1)    

    for i in range(0,20):
        client.subscribe("sala2/tecla"+str(i),1)

    print("Suscrito a los temas dificultad y tecla de 1 a 20")

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