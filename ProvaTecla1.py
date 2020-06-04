
import paho.mqtt.client as mqtt #important el client
import pygame
import time
import subprocess
import threading

pygame.mixer.init()	
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)

#Funció per a executar el servidor de mosquitto
#def mosquitto():
    #subprocess.call(mosquitto_path,'-v',shell=True)
#    subprocess.call(mosquitto_path,shell=True)

#Creació de un thread on s'executa el servidor mosquitto

#hilo = threading.Thread(target=mosquitto)    
#hilo.start()

DIFICULTAD=0 #variable dificultat, per defecte facil 0, 1 dificil


tecla1=False
tecla2=False
tecla3=False
tecla4=False
tecla5=False
tecla6=False
tecla7=False
tecla8=False
tecla9=False
tecla10=False
tecla11=False
tecla12=False
tecla13=False
tecla14=False
tecla15=False
tecla16=False
tecla17=False
tecla18=False
tecla19=False
tecla20=False

tecla1_1 = pygame.mixer.Sound('/home/pi/audio2/A1-1.ogg')
tecla1_2 = pygame.mixer.Sound('/home/pi/audio2/A1-2.ogg')
tecla1_3 = pygame.mixer.Sound('/home/pi/audio2/A1-3.ogg')
#tecla2_1 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla2_2 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla2_3 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla3_1 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla3_2 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla3_3 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla4_1 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla4_2 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla4_3 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla5_1 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla5_2 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla5_3 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla6_1 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
#tecla6_2 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
#tecla6_3 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
#tecla7_1 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla7_2 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla7_3 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla8_1 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla8_2 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla8_3 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla9_1 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla9_2 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla9_3 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla10_1 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla10_2 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla10_3 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla11_1 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
#tecla11_2 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
#tecla11_3 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
#tecla12_1 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla12_2 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla12_3 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla13_1 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla13_2 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla13_3 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla14_1 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla14_2 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla14_3 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla15_1 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla15_2 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla15_3 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla16_1 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
#tecla16_2 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
#tecla16_3 = pygame.mixer.Sound('/home/pi/audio2/A1.wav')
#tecla17_1 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla17_2 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla17_3 = pygame.mixer.Sound('/home/pi/audio2/A-1.wav')
#tecla18_1 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla18_2 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla18_3 = pygame.mixer.Sound('/home/pi/audio2/B1.wav')
#tecla19_1 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla19_2 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla19_3 = pygame.mixer.Sound('/home/pi/audio2/C1.wav')
#tecla20_1 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla20_2 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')
#tecla20_3 = pygame.mixer.Sound('/home/pi/audio2/C-1.wav')


def tecla1_inici():
    global tecla1
    tecla1=True
    pygame.mixer.Sound.play(tecla1_1)
    while(tecla1):
        pygame.mixer.Sound.play(tecla1_2)
    pygame.mixer.Sound.play(tecla1_3) 

def tecla2_inici():
    global tecla2
    tecla2=True
    pygame.mixer.Sound.play(tecla2_1)
    while(tecla2):
        pygame.mixer.Sound.play(tecla2_2)
    pygame.mixer.Sound.play(tecla2_3) 

def comensa():
    #time.sleep(63)
    pygame.mixer.music.load('/home/pi/audio2/A11.ogg') #obrir eixe archiu
    pygame.mixer.music.play()
    pygame.mixer.music.load('/home/pi/audio2/A12.ogg')
    pygame.mixer.music.play(-1)

def comensa1():
    pygame.mixer.Sound.play(sound1A1)    
    pygame.mixer.music.load('/home/pi/audio2/A12.ogg')
    pygame.mixer.music.play(-1)

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
            hilo = threading.Thread(target=tecla1_inici)
            hilo.start()
        elif mes == "0":
            print("ENTRA 1 en mes=0")
            global tecla1
            tecla1=False
    #elif topic == "sala2/tecla2":
    #    print("ENTRA en tecla2")
    #    if mes == "1":
    #        print("ENTRA 2 en mes=1")
    #        hilo = threading.Thread(target=tecla2_inici)
    #        hilo.start()
    #    elif mes == "0":
    #        print("ENTRA 2 en mes=0")
    #        global tecla2
    #        tecla2=False
    
def on_connect(client,userdata,flags,rc):
  
    client.subscribe("sala2/dificultad",1)    

    client.subscribe("sala2/tecla1",1)
#    for i in range(0,20):
#        client.subscribe("sala2/tecla"+str(i),1)

    print("Suscrito a los temas dificultad y tecla1")

broker_address="127.0.0.1" #ip del servidor
#broker_address="192.168.68.1" #ip del servidor
#broker_address="192.168.1.3"

print("Creando una estancia")
client = mqtt.Client("ProvaTecla1") #creant una estancia
client.on_message=on_message #cridant a on_message
client.on_connect=on_connect #cridant a on_connect
print("Conectando con el servidor")
client.connect(broker_address) #conectant-se al servidor 
client.loop_forever()
