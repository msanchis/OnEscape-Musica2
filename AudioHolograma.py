import paho.mqtt.client as mqtt #important el client
import pygame
import time
import subprocess
import threading

global client # Mosquitto_Client

pygame.mixer.init()	
pygame.mixer.pre_init(frequency=44100, size=-16, buffer=4096)

path = "/home/pi/"
#path = "C:\\Users\\Micky\\Documents\\Escape Room\\Sala2\\audioServidor\\"

DIFICULTAD=0 #variable dificultat, per defecte facil 0, 1 dificil
tiempoEspera=3 # variable para definir el tiempo de espera antes de reproducir sonido

intro_holograma = pygame.mixer.Sound(path+'03_INTRO_HOLOGRAMA.ogg')
final_holograma = pygame.mixer.Sound(path+'03_FINAL_HOLOGRAMA.ogg')
despedida_holograma = pygame.mixer.Sound(path+'03_DESPEDIDA_HOLOGRAMA.ogg')

companeros_encerrados = pygame.mixer.Sound(path+'COMPANEROS_ENCERRADOS.ogg')
dejad_organo = pygame.mixer.Sound(path+'DEJAD_ORGANO.ogg')
interpretar_emociones = pygame.mixer.Sound(path+'INTERPRETAR_EMOCIONES.ogg')
nada_en_pedestal = pygame.mixer.Sound(path+'NADA_EN_PEDESTAL.ogg')
nunca_llegareis = pygame.mixer.Sound(path+'NUNCA_LLEGAREIS.ogg')
truenos_animo = pygame.mixer.Sound(path+'TRUENOS_ANIMO.ogg')

eso_delicado = pygame.mixer.Sound(path+'ESO_DELICADO.ogg')
haciendo_noche = pygame.mixer.Sound(path+'HACIENDO_NOCHE.ogg')
mentiras_walkie = pygame.mixer.Sound(path+'MENTIRAS_WALKIE.ogg')
no_comunicacion = pygame.mixer.Sound(path+'NO_COMUNICACION.ogg')
objeto_usado = pygame.mixer.Sound(path+'OBJETO_USADO.ogg')
objetos_uso1 = pygame.mixer.Sound(path+'OBJETOS_1USO_1.ogg')
objetos_uso2 = pygame.mixer.Sound(path+'OBJETOS_1USO_2.ogg')
que_miras = pygame.mixer.Sound(path+'QUE_MIRAS.ogg')

claro_claro = pygame.mixer.Sound(path+'CLARO_CLARO.ogg')
cuanta_imaginacion = pygame.mixer.Sound(path+'CUANTA_IMAGINACION.ogg')
encerrados_por_vida = pygame.mixer.Sound(path+'ENCERRADOS_POR_VIDA.ogg')
perdiendo_tiempo = pygame.mixer.Sound(path+'PERDIENDO_TIEMPO.ogg')
sacar_companeros = pygame.mixer.Sound(path+'SACAR_COMPANEROS.ogg')

como_adivinado = pygame.mixer.Sound(path+'COMO_ADIVINADO.ogg')
eso_trampa = pygame.mixer.Sound(path+'ESO_TRAMPA.ogg')
imposible_averiguar = pygame.mixer.Sound(path+'IMPOSIBLE_AVERIGUAR.ogg')
no_adivinar = pygame.mixer.Sound(path+'NO_ADIVINAR.ogg')
os_maldigo = pygame.mixer.Sound(path+'OS_MALDIGO.ogg')
primeros_tan_lejos = pygame.mixer.Sound(path+'PRIMEROS_TAN_LEJOS.ogg')


def introHolograma():    
    pygame.mixer.Sound.play(intro_holograma)
def finalHolograma():    
    pygame.mixer.Sound.play(final_holograma)
def despedidaHolograma():    
    pygame.mixer.Sound.play(despedida_holograma)


def companerosEncerrados():
    pygame.mixer.Sound.play(companeros_encerrados)
def dejadOrgano():
    pygame.mixer.Sound.play(dejad_organo)
def interpretarEmociones():
    pygame.mixer.Sound.play(interpretar_emociones)
def nadaEnPedestal():
    pygame.mixer.Sound.play(nada_en_pedestal)
def nuncaLlegareis():
    pygame.mixer.Sound.play(nunca_llegareis)
def truenosAnimo():
    pygame.mixer.Sound.play(truenos_animo)


def esoDelicado():
    pygame.mixer.Sound.play(eso_delicado)
def haciendoNoche():
    pygame.mixer.Sound.play(haciendo_noche)
def mentirasWalkie():
    pygame.mixer.Sound.play(mentiras_walkie)
def noComunicacion():
    pygame.mixer.Sound.play(no_comunicacion)
def objetoUsado():
    pygame.mixer.Sound.play(objeto_usado)
def objetosUso1():
    pygame.mixer.Sound.play(objetos_uso1)
def objetosUso2():
    pygame.mixer.Sound.play(objetos_uso2)
def queMiras():
    pygame.mixer.Sound.play(que_miras)


def claroClaro():
    pygame.mixer.Sound.play(claro_claro)
def cuantaImaginacion():
    pygame.mixer.Sound.play(cuanta_imaginacion)
def encerradosPorVida():
    pygame.mixer.Sound.play(encerrados_por_vida)
def perdiendoTiempo():
    pygame.mixer.Sound.play(perdiendo_tiempo)
def sacarCompaneros():
    pygame.mixer.Sound.play(sacar_companeros)


def comoAdivinado():
    pygame.mixer.Sound.play(como_adivinado)
def esoTrampa():
    pygame.mixer.Sound.play(eso_trampa)
def imposibleAveriguar():
    pygame.mixer.Sound.play(imposible_averiguar)
def noAdivinar():
    pygame.mixer.Sound.play(no_adivinar)
def osMaldigo():
    pygame.mixer.Sound.play(os_maldigo)
def primerosTanLejos():
    pygame.mixer.Sound.play(primeros_tan_lejos)


def on_message(client, userdata, message):    

    global DIFICULTAD
    global tiempoEspera
    topic = str(message.topic)
    mes = str(message.payload.decode("utf-8"))
    if topic == "sala2/dificultad":
        if mes == "1":
            DIFICULTAD="1" #dificil
        else:
            DIFICULTAD="0" #facil
    elif topic == "sala2/introHolograma":        
        t = threading.Timer(tiempoEspera,introHolograma)                
        t.start()
    elif topic == "sala2/finalHolograma":        
        t = threading.Timer(tiempoEspera,finalHolograma)                
        t.start()
    elif topic == "sala2/despedidaHolograma":        
        t = threading.Timer(tiempoEspera,despedidaHolograma)                
        t.start()       
    elif topic == "sala2/dejadOrgano":        
        t = threading.Timer(tiempoEspera,dejadOrgano)                
        t.start()  
    elif topic == "sala2/interpretarEmociones":        
        t = threading.Timer(tiempoEspera,interpretarEmociones)                
        t.start()  
    elif topic == "sala2/nadaEnPedestal":        
        t = threading.Timer(tiempoEspera,nadaEnPedestal)                
        t.start()  
    elif topic == "sala2/nuncaLlegareis":        
        t = threading.Timer(tiempoEspera,nuncaLlegareis)                
        t.start()  
    elif topic == "sala2/truenosAnimo":        
        t = threading.Timer(tiempoEspera,truenosAnimo)                
        t.start() 
    elif topic == "sala2/esoEsDelicado":        
        t = threading.Timer(tiempoEspera,esoEsDelicado)                
        t.start() 
    elif topic == "sala2/haciendoNoche":        
        t = threading.Timer(tiempoEspera,haciendoNoche)                
        t.start() 
    elif topic == "sala2/mentirasWalkie":        
        t = threading.Timer(tiempoEspera,mentirasWalkie)                
        t.start() 
    elif topic == "sala2/noComunicacion":        
        t = threading.Timer(tiempoEspera,noComunicacion)                
        t.start() 
    elif topic == "sala2/objetoUsado":        
        t = threading.Timer(tiempoEspera,objetoUsado)                
        t.start() 
    elif topic == "sala2/objetos1Uso":        
        t = threading.Timer(tiempoEspera,objetos1Uso)                
        t.start() 
    elif topic == "sala2/objetos1Uso2":        
        t = threading.Timer(tiempoEspera,objetos1Uso2)                
        t.start() 
    elif topic == "sala2/companerosEncerrados":        
        t = threading.Timer(tiempoEspera,companerosEncerrados)                
        t.start() 
    elif topic == "sala2/sacarCompaneros":        
        t = threading.Timer(tiempoEspera,sacarCompaneros)                
        t.start() 
    elif topic == "sala2/queMiras":        
        t = threading.Timer(tiempoEspera,queMiras)                
        t.start() 
    elif topic == "sala2/claroClaro":        
        t = threading.Timer(tiempoEspera,claroClaro)                
        t.start() 
    elif topic == "sala2/cuantaImaginacion":        
        t = threading.Timer(tiempoEspera,cuantaImaginacion)                
        t.start() 
    elif topic == "sala2/encerradosPorVida":        
        t = threading.Timer(tiempoEspera,nuncaLlegareis)                
        t.start() 
    elif topic == "sala2/perdiendoTiempo":        
        t = threading.Timer(tiempoEspera,perdiendoTiempo)                
        t.start()
    elif topic == "sala2/comoAdivinado":        
        t = threading.Timer(tiempoEspera,comoAdivinado)                
        t.start()
    elif topic == "sala2/esoEsTrampa":        
        t = threading.Timer(tiempoEspera,esoEsTrampa)                
        t.start()
    elif topic == "sala2/imposibleAveriguar":        
        t = threading.Timer(tiempoEspera,imposibleAveriguar)                
        t.start()
    elif topic == "sala2/noAdivinar":        
        t = threading.Timer(tiempoEspera,noAdivinar)                
        t.start()
    elif topic == "sala2/osMaldigo":        
        t = threading.Timer(tiempoEspera,osMaldigo)                
        t.start() 
    elif topic == "sala2/primerosTanLejos":        
        t = threading.Timer(tiempoEspera,primerosTanLejos)                
        t.start()
    elif topic == "sala2/tiempoAcabando":        
        t = threading.Timer(tiempoEspera,tiempoAcabando)                
        t.start()    
     
def on_connect(client,userdata,flags,rc):
  
    client.subscribe("sala2/dificultad",1)
    client.subscribe("sala2/comensa",1)
    client.subscribe("sala2/introHolograma",1)
    client.subscribe("sala2/dejadOrgano",1)
    client.subscribe("sala2/interpretarEmociones",1)
    client.subscribe("sala2/nadaEnPedestal",1)
    client.subscribe("sala2/nuncaLlegareis",1)
    client.subscribe("sala2/truenosAnimo",1)
    client.subscribe("sala2/esoEsDelicado",1)
    client.subscribe("sala2/haciendoNoche",1)
    client.subscribe("sala2/mentirasWalkie",1)
    client.subscribe("sala2/noComunicacion",1)
    client.subscribe("sala2/objetoUsado",1)
    client.subscribe("sala2/objetos1Uso",1)
    client.subscribe("sala2/objetos1Uso2",1)
    client.subscribe("sala2/companerosEncerrados",1)
    client.subscribe("sala2/sacarCompaneros",1)
    client.subscribe("sala2/queMiras",1)
    client.subscribe("sala2/claroClaro",1)
    client.subscribe("sala2/cuantaImaginacion",1)
    client.subscribe("sala2/encerradosPorVida",1)
    client.subscribe("sala2/perdiendoTiempo",1)
    client.subscribe("sala2/comoAdivinado",1)
    client.subscribe("sala2/esoEsTrampa",1)
    client.subscribe("sala2/imposibleAveriguar",1)
    client.subscribe("sala2/noAdivinar",1)
    client.subscribe("sala2/osMaldigo",1)
    client.subscribe("sala2/primerosTanLejos",1)
    client.subscribe("sala2/tiempoAcabando",1)
    client.subscribe("sala2/despedidaHolograma",1)
    client.subscribe("sala2/finalHolograma",1)    

    

time.sleep(5)
#broker_address="192.168.68.55" #ip del servidor
#broker_address="192.168.1.2"
broker_address="127.0.0.1"

client = mqtt.Client("AudioHolograma") #creant una estancia
client.on_message=on_message #cridant a on_message
client.on_connect=on_connect #cridant a on_connect

client.connect(broker_address) #conectant-se al servidor 
client.loop_forever()
