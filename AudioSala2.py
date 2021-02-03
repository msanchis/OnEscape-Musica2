#TODO Comprobar si les 5 primeres tecles "greus" sonen més fort que la resta 
# set_volume 1.0 a Sound i a Channel
# set_volume de music esta inicialment a 0.5

import paho.mqtt.client as mqtt #important el client
import pygame
import time
import subprocess
import threading

mosquitto_path='mosquitto -v'
def mosquito():
    subprocess.call(mosquitto_path,shell=True)

fil = threading.Thread(target=mosquito)
#fil.start()

client = None

pygame.mixer.init()	
pygame.mixer.pre_init(frequency=44100, size=-16, channels=20, buffer=4096)

#Comprovar que així funciona
#pygame.mixer.set_num_channels(20)

#path = "/home/pi/"
#pathTecla = "/home/pi/audio2/"
path = "C:\\Users\\Micky\\Documents\\Escape Room\\Sala2\\audioServidor\\"
pathTecla = "C:\\Users\\Micky\\Documents\\Escape Room\\Sala2\\audioServidor\\audio2\\"

DIFICULTAD=0 #variable dificultat, per defecte facil 0, 1 dificil

#SONS 20 TECLES ORGAN
tecla1_1 = pygame.mixer.Sound(pathTecla+'G2.ogg')
tecla1_1.set_volume(1.0)
tecla2_1 = pygame.mixer.Sound(pathTecla+'F#2.ogg')
tecla2_1.set_volume(1.0)
tecla3_1 = pygame.mixer.Sound(pathTecla+'F2.ogg')
tecla3_1.set_volume(1.0)
tecla4_1 = pygame.mixer.Sound(pathTecla+'E2.ogg')
tecla4_1.set_volume(1.0)
tecla5_1 = pygame.mixer.Sound(pathTecla+'D#2.ogg')
tecla5_1.set_volume(1.0)
tecla6_1 = pygame.mixer.Sound(pathTecla+'D2.ogg')
tecla7_1 = pygame.mixer.Sound(pathTecla+'C#2.ogg')
tecla8_1 = pygame.mixer.Sound(pathTecla+'C2.ogg')
tecla9_1 = pygame.mixer.Sound(pathTecla+'B1.ogg')
tecla10_1 = pygame.mixer.Sound(pathTecla+'A#1.ogg')
tecla11_1 = pygame.mixer.Sound(pathTecla+'A1.ogg')
tecla12_1 = pygame.mixer.Sound(pathTecla+'G#1.ogg')
tecla13_1 = pygame.mixer.Sound(pathTecla+'G1.ogg')
tecla14_1 = pygame.mixer.Sound(pathTecla+'F#1.ogg')
tecla15_1 = pygame.mixer.Sound(pathTecla+'F1.ogg')
tecla16_1 = pygame.mixer.Sound(pathTecla+'E1.ogg')
tecla17_1 = pygame.mixer.Sound(pathTecla+'D#1.ogg')
tecla18_1 = pygame.mixer.Sound(pathTecla+'D1.ogg')
tecla19_1 = pygame.mixer.Sound(pathTecla+'C#1.ogg')
tecla20_1 = pygame.mixer.Sound(pathTecla+'C1.ogg')

holo = pygame.mixer.Sound(path+'holograma.wav')
holo1 = pygame.mixer.Sound(path+'holograma1.ogg')
holo2 = pygame.mixer.Sound(path+'holograma2.ogg')

trona = pygame.mixer.Sound(path+'trona.wav')
llamp = pygame.mixer.Sound(path+'llamp.wav')
plutja = pygame.mixer.Sound(path+'plutja.wav')

bucle1 = pygame.mixer.Sound(path+'bucle1.ogg')
bucle2 = pygame.mixer.Sound(path+'bucle2.ogg')



def tormenta1():    
    pygame.mixer.Sound.play(trona)

def relampago1():    
    time.sleep(1)
    pygame.mixer.Sound.play(llamp)

def tormenta():
    client.publish("sala2/trona","1")    
    pygame.mixer.Sound.play(trona)

def relampago():
    client.publish("sala2/llamp","1")
    time.sleep(1)
    pygame.mixer.Sound.play(llamp)

def comensa():    
    pygame.mixer.music.set_volume(0.5) #comesar amb 0.5 de volumen
    pygame.mixer.music.load(path+'plutja.wav') #obrir el archiu 15 MINUTS 900 secs        
    pygame.mixer.music.play()    

def cambioMusica():
    pygame.mixer.music.fadeout(3000)    
    pygame.mixer.music.load(path+'ambient1.ogg') #reproduim 10 MINUTS
    pygame.mixer.music.play()
    pygame.mixer.music.queue(path+'bucle2.ogg') #posem en cua 2 MINUTS               

def cambioMusica2():    
    pygame.mixer.music.fadeout(3000)    
    pygame.mixer.music.load(path+'bucle2.ogg')    
    pygame.mixer.music.play(8) #repetim 9 vegades 10 MINUTS
    pygame.mixer.music.queue(path+'bucle1.ogg') #posem en cua 2 MINUTS               

def cambioMusica3():
    pygame.mixer.music.fadeout(3000)    
    pygame.mixer.music.load(path+'bucle1.ogg')    
    pygame.mixer.music.play(8) #repetim 9 vegades 10 MINUTS

def holograma():
    pygame.mixer.Sound.play(holo)

def holograma1():
    pygame.mixer.Sound.play(holo1)

def holograma2():
    pygame.mixer.Sound.play(holo2)

def buc1():  
    pygame.mixer.Sound.play(bucle1)

def buc2():
    pygame.mixer.Sound.play(bucle2)

        
def on_message(client, userdata, message):    

    global DIFICULTAD
    topic = str(message.topic)
    mes = str(message.payload.decode("utf-8"))
    print(topic+ " " + mes)
    if topic == "sala2/dificultad":
        if mes == "1":
            DIFICULTAD="1" #dificil
        else:
            DIFICULTAD="0" #facil
    elif topic == "sala2/comensa":        
        hilo = threading.Thread(target=comensa)
        hilo.start()        

        t = threading.Timer(30,tormenta)                
        t.start()
        
        t = threading.Timer(90,tormenta)
        t.start()
        
        t = threading.Timer(120,relampago)
        t.start()

        t = threading.Timer(300,tormenta)
        t.start()

        t= threading.Timer(600,tormenta)
        t.start()
        
        t= threading.Timer(900,tormenta)
        t.start()

        t= threading.Timer(1200,tormenta)
        t.start()

        t= threading.Timer(800, cambioMusica)
        t.start()

        t= threading.Timer(2000, cambioMusica2)
        t.start()

        t= threading.Timer(2500, cambioMusica3)
        t.start()        


    elif topic == "sala2/inici":
        hilo = threading.Thread(target=comensa)
        hilo.start()

    elif topic == "sala2/holograma":
        hilo = threading.Thread(target=holograma)
        hilo.start()

    elif topic == "sala2/holograma1":
        hilo = threading.Thread(target=holograma1)
        hilo.start()

    elif topic == "sala2/holograma2":
        hilo = threading.Thread(target=holograma2)
        hilo.start()   

    elif topic == "sala2/trona":
        hilo = threading.Thread(target=tormenta1)
        hilo.start()

    elif topic == "sala2/llamp":
        hilo = threading.Thread(target=relampago1)
        hilo.start()

    elif topic == "sala2/bucle1":
        hilo = threading.Thread(target=buc1)
        hilo.start()

    elif topic == "sala2/bucle2":
        hilo = threading.Thread(target=buc2)
        hilo.start()

    elif topic == "sala2/tecla1":
        if mes == "0":
            if not pygame.mixer.Channel(0).get_busy():
                pygame.mixer.Channel(0).set_volume(1.0)
                pygame.mixer.Channel(0).play(tecla1_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(0).fadeout(400)
    elif topic == "sala2/tecla2":
        if mes == "0":
            if not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).set_volume(1.0)
                pygame.mixer.Channel(1).play(tecla2_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(1).fadeout(400)
    elif topic == "sala2/tecla3":
        if mes == "0":
            if not pygame.mixer.Channel(2).get_busy():
                pygame.mixer.Channel(2).set_volume(1.0)
                pygame.mixer.Channel(2).play(tecla3_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(2).fadeout(400)
    elif topic == "sala2/tecla4":
        if mes == "0":
            if not pygame.mixer.Channel(3).get_busy():
                pygame.mixer.Channel(3).set_volume(1.0)
                pygame.mixer.Channel(3).play(tecla4_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(3).fadeout(400)
    elif topic == "sala2/tecla5":
        if mes == "0":
            if not pygame.mixer.Channel(4).get_busy():
                pygame.mixer.Channel(4).set_volume(1.0)
                pygame.mixer.Channel(4).play(tecla5_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(4).fadeout(400)
    elif topic == "sala2/tecla6":
        if mes == "0":
            if not pygame.mixer.Channel(5).get_busy():
                pygame.mixer.Channel(5).play(tecla6_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(5).fadeout(400)
    elif topic == "sala2/tecla7":
        if mes == "0":
            if not pygame.mixer.Channel(6).get_busy():
                pygame.mixer.Channel(6).play(tecla7_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(6).fadeout(400)
    elif topic == "sala2/tecla8":
        if mes == "0":
            if not pygame.mixer.Channel(7).get_busy():
                pygame.mixer.Channel(7).play(tecla8_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(7).fadeout(400)
    elif topic == "sala2/tecla9":
        if mes == "0":
            if not pygame.mixer.Channel(8).get_busy():
                pygame.mixer.Channel(8).play(tecla9_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(8).fadeout(400)
    elif topic == "sala2/tecla10":
        if mes == "0":
            if not pygame.mixer.Channel(9).get_busy():
                pygame.mixer.Channel(9).play(tecla10_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(9).fadeout(400)
    elif topic == "sala2/tecla11":
        if mes == "0":
            if not pygame.mixer.Channel(10).get_busy():
                pygame.mixer.Channel(10).play(tecla11_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(10).fadeout(400)
    elif topic == "sala2/tecla12":
        if mes == "0":
            if not pygame.mixer.Channel(11).get_busy():
                pygame.mixer.Channel(11).play(tecla12_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(11).fadeout(400)
    elif topic == "sala2/tecla13":
        if mes == "0":
            if not pygame.mixer.Channel(12).get_busy():
                pygame.mixer.Channel(12).play(tecla13_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(12).fadeout(400)
    elif topic == "sala2/tecla14":
        if mes == "0":
            if not pygame.mixer.Channel(13).get_busy():
                pygame.mixer.Channel(13).play(tecla14_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(13).fadeout(400)
    elif topic == "sala2/tecla15":
        if mes == "0":
            if not pygame.mixer.Channel(14).get_busy():
                pygame.mixer.Channel(14).play(tecla15_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(14).fadeout(400)
    elif topic == "sala2/tecla16":
        if mes == "0":
            if not pygame.mixer.Channel(15).get_busy():
                pygame.mixer.Channel(15).play(tecla16_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(15).fadeout(400)
    elif topic == "sala2/tecla17":
        if mes == "0":
            if not pygame.mixer.Channel(16).get_busy():
                pygame.mixer.Channel(16).play(tecla17_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(16).fadeout(400)
    elif topic == "sala2/tecla18":
        if mes == "0":
            if not pygame.mixer.Channel(17).get_busy():
                pygame.mixer.Channel(17).play(tecla18_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(17).fadeout(400)
    elif topic == "sala2/tecla19":
        if mes == "0":
            if not pygame.mixer.Channel(18).get_busy():
                pygame.mixer.Channel(18).play(tecla19_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(18).fadeout(400)
    elif topic == "sala2/tecla20":
        if mes == "0":
            if not pygame.mixer.Channel(19).get_busy():
                pygame.mixer.Channel(19).play(tecla20_1,-1,20000)
        elif mes == "1":
            pygame.mixer.Channel(19).fadeout(400)
    elif topic == "sala2/paraMusica":
        pygame.mixer.music.stop()



def on_connect(client,userdata,flags,rc):
    for i in range(1,21):
        client.subscribe("sala2/tecla"+str(i),1)

    client.subscribe("sala2/comensa",1)
    client.subscribe("sala2/inici",1)

    client.subscribe("sala2/holograma",1)
    client.subscribe("sala2/holograma1",1)
    client.subscribe("sala2/holograma2",1)

    client.subscribe("sala2/trona",1)
    client.subscribe("sala2/llamp",1)
    client.subscribe("sala2/cova",1)

    client.subscribe("sala2/bucle1",1)
    client.subscribe("sala2/bucle2",1)

    client.subscribe("sala2/paraMusica")

time.sleep(5)
#broker_address="192.168.68.55" #ip del servidor
#broker_address="192.168.1.2"
broker_address="127.0.0.1"
print("Creando una estancia")

client = mqtt.Client("AudioSala2") #creant una estancia
client.on_message=on_message #cridant a on_message
client.on_connect=on_connect #cridant a on_connect

print("Conectando con el servidor")

client.connect(broker_address) #conectant-se al servidor 
client.loop_forever()
