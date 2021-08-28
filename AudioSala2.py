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
fil.start()

global client # Mosquitto_Client
global lento1
lento1=0
global lento2
lento2=0
global t # Thread musica

pygame.mixer.init()	
pygame.mixer.pre_init(frequency=44100, size=-16, channels=20, buffer=4096)

#Comprovar que així funciona
pygame.mixer.set_num_channels(20)

path = "/home/pi/"
pathTecla = "/home/pi/audio2/"
#path = "C:\\Users\\Micky\\Documents\\Escape Room\\Sala2\\audioServidor\\"
#pathTecla = "C:\\Users\\Micky\\Documents\\Escape Room\\Sala2\\audioServidor\\audio2\\"

DIFICULTAD=0 #variable dificultat, per defecte facil 0, 1 dificil

#SONS 20 TECLES ORGAN
tecla1_1 = pygame.mixer.Sound(pathTecla+'G2.ogg')
tecla2_1 = pygame.mixer.Sound(pathTecla+'F#2.ogg')
tecla3_1 = pygame.mixer.Sound(pathTecla+'F2.ogg')
tecla4_1 = pygame.mixer.Sound(pathTecla+'E2.ogg')
tecla5_1 = pygame.mixer.Sound(pathTecla+'D#2.ogg')
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

trona = pygame.mixer.Sound(path+'trona.wav')
llamp = pygame.mixer.Sound(path+'llamp.wav')

inicio_pedestal_S = pygame.mixer.Sound(path+'05_FX_INICIO_PEDESTAL.ogg')
reliquia_colocada_S = pygame.mixer.Sound(path+'05_FX_RELIQUIA_COLOCADA.ogg')
encuentran_corazon_S = pygame.mixer.Sound(path+'05_FX_ENCUENTRAN_CORAZON.ogg')

calavera_inicial_S = pygame.mixer.Sound(path+'08_FX_CALAVERA_INICIAL.ogg')
calavera_bajando1_S = pygame.mixer.Sound(path+'08_FX_CALAVERA_BAJANDO_1.ogg')
calavera_bajando2_S = pygame.mixer.Sound(path+'08_FX_CALAVERA_BAJANDO_2.ogg')
calavera_lento1_S = pygame.mixer.Sound(path+'08_FX_CALAVERA_LENTO_1.ogg')
calavera_lento2_S = pygame.mixer.Sound(path+'08_FX_CALAVERA_LENTO_2.ogg')
calavera_conseguido_S = pygame.mixer.Sound(path+'08_FX_CALAVERA_CONSEGUIDO.ogg')
calavera_llave_S = pygame.mixer.Sound(path+'08_FX_CALAVERA_LLAVE_AIRE.ogg')
calavera_prisa_S = pygame.mixer.Sound(path+'08_FX_CALAVERA_PRISA.ogg')

def tormenta1():    
    pygame.mixer.Sound.play(trona)

def calavera_lento1():
    global lento1
    if lento1 == 0:
        pygame.mixer.Sound.play(calavera_lento1_S)
    else:
        lento1=0

def calavera_lento2():
    global lento2
    if lento2 == 0:
        pygame.mixer.Sound.play(calavera_lento2_S)
    else:
        lento2=0

def calavera_bajando1():
    pygame.mixer.Sound.play(calavera_bajando1_S)

def calavera_bajando2():
    pygame.mixer.Sound.play(calavera_bajando2_S)

def calavera_prisa():
    pygame.mixer.Sound.play(calavera_prisa_S)

def calavera_llave():
    pygame.mixer.Sound.play(calavera_llave_S)

def calavera_inicial():
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.Sound.play(calavera_inicial_S)
    time.sleep(6)
    pygame.mixer.music.set_volume(0.2)

def calavera_conseguido():
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.Sound.play(calavera_conseguido_S)
    time.sleep(6)
    pygame.mixer.music.load(path+'10_MUSICA_DESPUES_PINCHOS_BUCLE.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

def relampago1():    
    time.sleep(0.6)
    pygame.mixer.Sound.play(llamp)

def tormenta():
    client.publish("sala2/trona","1")    
    pygame.mixer.Sound.play(trona)

def relampago():
    client.publish("sala2/llamp","1")
    time.sleep(0.6)
    pygame.mixer.Sound.play(llamp)

def inicio_pedestal():
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.Sound.play(inicio_pedestal_S) # inicio Pedestal
    time.sleep(9)
    pygame.mixer.music.set_volume(0.3)

def reliquia_colocada():
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.Sound.play(reliquia_colocada_S) # reliquias de la 1 a la 5
    time.sleep(3)
    pygame.mixer.music.set_volume(0.2)

def encuentran_corazon():
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.Sound.play(encuentran_corazon_S) # reliquia 6
    pygame.mixer.music.load(path+'11_MUSICA_ENCUENTRAN_CORAZON.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music_set_volume(0.2)

def derrumbe():
    pygame.mixer.music.fadeout(5000)
    pygame.mixer.music.load(path+'12_MUSICA_DERRUMBE.ogg')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)

def musica_triunfo_final():
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.load(path+'13_MUSICA_TRIUNFO_FINAL.ogg')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)

def musica_pasadizo():
    pygame.mixer.music.fadeout(5000)
    pygame.mixer.music.load(path+'06_MUSICA_PASADIZO_BUCLE.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

def comensa():    
    pygame.mixer.music.load(path+'plutja.wav') #obrir el archiu 15 MINUTS 900 secs        
    pygame.mixer.music.play(-1)    
    pygame.mixer.music.set_volume(0.3)

def para():
    pygame.mixer.music.fadeout(3000)

def musica_inicial():
    pygame.mixer.music.load(path+'04_MUSICA_INICIAL_BUCLE.ogg') 
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)    

def musica_pinchos():
    pygame.mixer.music.fadeout(100)    
    pygame.mixer.music.load(path+'07_MUSICA_BAJANDO_PINCHOS.ogg') #reproduim 10 
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)


def despues_pinchos():    
    pygame.mixer.music.fadeout(5000) 
    pygame.mixer.music.load(path+'10_MUSICA_DESPUES_PINCHOS_BUCLE.ogg')    
    pygame.mixer.music.play() #
    pygame.mixer.music.set_volume(0.2)

def cambia_musica():
    pygame.mixer.music.fadeout(5000)
    h = threading.Timer(10, musica_inicial)
    h.start()

def holograma():
    pygame.mixer.music.fadeout(5000)
    pygame.mixer.Sound.play(holo)
    h = threading.Timer(10, musica_inicial)
    h.start()

def holograma1():
    pygame.mixer.Sound.play(holo1)

def holograma2():
    pygame.mixer.Sound.play(holo2)

def acords():
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.Sound.play(organo1)
    time.sleep(10)
    pygame.mixer.music.set_volume(0.2)
        
def triunfo_final():
    pygame.mixer.music.fadeout(200)
    pygame.mixer.music.load(path+'13_MUSICA_TRIUNFO_FINAL.ogg')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)

def on_message(client, userdata, message):    

    global DIFICULTAD
    topic = str(message.topic)
    mes = str(message.payload.decode("utf-8"))
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
        
        t = threading.Timer(100,tormenta)
        t.start()

        t = threading.Timer(120,relampago)
        t.start()

        t = threading.Timer(130,tormenta)
        t.start()

        t = threading.Timer(300,tormenta)
        t.start()

    elif topic == "sala2/cambiaMusica":
        hilo = threading.Thread(target=cambia_musica)
        hilo.start()

    elif topic == "sala2/tancaPortaCaraVeritat":
        hilo = threading.Thread(target=musica_pasadizo)
        hilo.start()
        
    elif topic == "sala2/iniciaPunxos":
        hilo = threading.Thread(target=musica_pinchos)
        hilo.start()

    elif topic == "sala2/punxos1": #Revisar topic
        hilo = threading.Thread(target=calavera_bajando1)
        hilo.start()
        hilo = threading.Timer(12,calavera_lento1)
        hilo.start()

    elif topic == "sala2/punxos2": #Revisar topic
        hilo = threading.Thread(target=calavera_bajando2)
        hilo.start()
        hilo = threading.Timer(12,calavera_lento2)
        hilo.start()

    elif topic == "sala2/punxos3": #Revisar topic
        hilo = threading.Thread(target=calavera_bajando1)
        hilo.start()
        hilo = threading.Timer(12,calavera_lento1)
        hilo.start()

    elif topic == "sala2/punxos4": #Revisar topic
        hilo = threading.Thread(target=calavera_bajando2)
        hilo.start()
        hilo = threading.Timer(12,calavera_lento2)
        hilo.start()

    elif topic == "sala2/finalPunxos":
        hilo = threading.Timer(60,calavera_prisa)
        hilo.start()
    
    elif topic == "sala2/calaveraLlave":
        hilo = threading.Thread(target=calavera_llave)
        hilo.start()

    elif topic in ["sala2/activaPuzzle1","sala2/estat1Pedestal"]:        
        hilo = threading.Thread(target=inicio_pedestal)
        hilo.start()
    
    elif topic in ["sala2/reliquia1","sala2/reliquia2","sala2/reliquia3","sala2/reliquia4","sala2/reliquia5"]:
        hilo = threading.Thread(target=reliquia_colocada)
        hilo.start()        

    elif topic == "sala2/reliquia6":
        hilo = threading.Thread(target=encuentran_corazon)
        hilo.start()

    elif topic == "sala2/acordCorrecte":
        global lento1
        lento1=1
        global lento2
        lento2=1
        hilo = threading.Thread(target=calavera_conseguido)
        hilo.start()
        
    elif topic == "sala2/activaOrgan":
        hilo = threading.Thread(target=calavera_inicial)
        hilo.start()

    elif topic == "sala2/detectaCor":
        hilo = threading.Thread(target=derrumbe)
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

    elif topic == "sala2/triunfoFinal":
        hilo = threading.Thread(target=musica_triunfo_final)
        hilo.start()

    elif topic == "sala2/activaOrgan":
        hilo = threading.Thread(target=acords)
        hilo.start()

    elif topic == "sala2/tecla1":
        if mes == "0":
            if not pygame.mixer.Channel(0).get_busy():
                #pygame.mixer.Channel(0).set_volume(1.0)
                pygame.mixer.Channel(0).play(tecla1_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(0).fadeout(400)
    elif topic == "sala2/tecla2":
        if mes == "0":
            if not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(tecla2_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(1).fadeout(400)
    elif topic == "sala2/tecla3":
        if mes == "0":
            if not pygame.mixer.Channel(2).get_busy():
                pygame.mixer.Channel(2).play(tecla3_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(2).fadeout(400)
    elif topic == "sala2/tecla4":
        if mes == "0":
            if not pygame.mixer.Channel(3).get_busy():
                pygame.mixer.Channel(3).play(tecla4_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(3).fadeout(400)
    elif topic == "sala2/tecla5":
        if mes == "0":
            if not pygame.mixer.Channel(4).get_busy():
                pygame.mixer.Channel(4).play(tecla5_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(4).fadeout(400)
    elif topic == "sala2/tecla6":
        if mes == "0":
            if not pygame.mixer.Channel(5).get_busy():
                pygame.mixer.Channel(5).play(tecla6_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(5).fadeout(400)
    elif topic == "sala2/tecla7":
        if mes == "0":
            if not pygame.mixer.Channel(6).get_busy():
                pygame.mixer.Channel(6).play(tecla7_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(6).fadeout(400)
    elif topic == "sala2/tecla8":
        if mes == "0":
            if not pygame.mixer.Channel(7).get_busy():
                pygame.mixer.Channel(7).play(tecla8_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(7).fadeout(400)
    elif topic == "sala2/tecla9":
        if mes == "0":
            if not pygame.mixer.Channel(8).get_busy():
                pygame.mixer.Channel(8).play(tecla9_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(8).fadeout(400)
    elif topic == "sala2/tecla10":
        if mes == "0":
            if not pygame.mixer.Channel(9).get_busy():
                pygame.mixer.Channel(9).play(tecla10_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(9).fadeout(400)
    elif topic == "sala2/tecla11":
        if mes == "0":
            if not pygame.mixer.Channel(10).get_busy():
                pygame.mixer.Channel(10).play(tecla11_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(10).fadeout(400)
    elif topic == "sala2/tecla12":
        if mes == "0":
            if not pygame.mixer.Channel(11).get_busy():
                pygame.mixer.Channel(11).play(tecla12_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(11).fadeout(400)
    elif topic == "sala2/tecla13":
        if mes == "0":
            if not pygame.mixer.Channel(12).get_busy():
                pygame.mixer.Channel(12).play(tecla13_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(12).fadeout(400)
    elif topic == "sala2/tecla14":
        if mes == "0":
            if not pygame.mixer.Channel(13).get_busy():
                pygame.mixer.Channel(13).play(tecla14_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(13).fadeout(400)
    elif topic == "sala2/tecla15":
        if mes == "0":
            if not pygame.mixer.Channel(14).get_busy():
                pygame.mixer.Channel(14).play(tecla15_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(14).fadeout(400)
    elif topic == "sala2/tecla16":
        if mes == "0":
            if not pygame.mixer.Channel(15).get_busy():
                pygame.mixer.Channel(15).play(tecla16_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(15).fadeout(400)
    elif topic == "sala2/tecla17":
        if mes == "0":
            if not pygame.mixer.Channel(16).get_busy():
                pygame.mixer.Channel(16).play(tecla17_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(16).fadeout(400)
    elif topic == "sala2/tecla18":
        if mes == "0":
            if not pygame.mixer.Channel(17).get_busy():
                pygame.mixer.Channel(17).play(tecla18_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(17).fadeout(400)
    elif topic == "sala2/tecla19":
        if mes == "0":
            if not pygame.mixer.Channel(18).get_busy():
                pygame.mixer.Channel(18).play(tecla19_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(18).fadeout(400)
    elif topic == "sala2/tecla20":
        if mes == "0":
            if not pygame.mixer.Channel(19).get_busy():
                pygame.mixer.Channel(19).play(tecla20_1,-1,7000)
        elif mes == "1":
            pygame.mixer.Channel(19).fadeout(400)
    elif topic == "sala2/paraMusica":
        pygame.mixer.music.stop()



def on_connect(client,userdata,flags,rc):
    for i in range(1,21):
        client.subscribe("sala2/tecla"+str(i),1)

    client.subscribe("sala2/comensa",1)
    client.subscribe("sala2/cambiaMusica",1)
    client.subscribe("sala2/trona",1)
    client.subscribe("sala2/llamp",1)

    client.subscribe("sala2/activaPuzzle1",1)
    client.subscribe("sala2/estat1Pedestal",1)
    client.subscribe("sala2/holograma",1)
    client.subscribe("sala2/holograma1",1)
    client.subscribe("sala2/holograma2",1)
    client.subscribe("sala2/tancaPortaCaraVeritat",1)

    client.subscribe("sala2/reliquia1",1)
    client.subscribe("sala2/reliquia2",1)
    client.subscribe("sala2/reliquia3",1)
    client.subscribe("sala2/reliquia4",1)
    client.subscribe("sala2/reliquia5",1)
    client.subscribe("sala2/reliquia6",1)


    #Revisar nom topics
    client.subscribe("sala2/punxos1")
    client.subscribe("sala2/punxos2")
    client.subscribe("sala2/punxos3")
    client.subscribe("sala2/punxos4")
    #REVISAR
    client.subscribe("sala2/calaveraLlave")

    client.subscribe("sala2/acordCorrecte",1)

    client.subscribe("sala2/detectaCor",1)

    client.subscribe("sala2/iniciaPunxos",1)
    client.subscribe("sala2/finalPunxos",1)
    client.subscribe("sala2/activaOrgan",1)

    client.subscribe("sala2/paraMusica",1)
    client.subscribe("sala2/triunfoFinal",1)

time.sleep(5)
#broker_address="192.168.68.55" #ip del servidor
#broker_address="192.168.1.2"
broker_address="127.0.0.1"

client = mqtt.Client("AudioSala2") #creant una estancia
client.on_message=on_message #cridant a on_message
client.on_connect=on_connect #cridant a on_connect

client.connect(broker_address) #conectant-se al servidor 
client.loop_forever()
