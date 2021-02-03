#!/bin/bash

#sleep 10 
echo "Iniciant clientsReproductors..."

source /home/pi/servidorMusica/bin/activate

/usr/bin/python3 /home/pi/AudioSala2.py &
/usr/bin/python3 /home/pi/audio2/Organo.py &

deactivate

#echo "..."
#python /home/pi/audio/ClientReproductorMusica.py &

echo "INICIALITZATS!!"
