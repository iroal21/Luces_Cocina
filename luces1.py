# GPIO 24 PULSADOR1
# GPIO 17 PULSADOR2
# GPIO 27 PULSADOR3
# GPIO 9 PULSADOR4

# GPIO 18 LED1
# GPIO 22 LED2
# GPIO 10 LED3
# GPIO 25 LED4


import RPi.GPIO as GPIO
import time
from mpyg321.mpyg321 import MPyg321Player
from time import sleep
from threading import Thread

musica = MPyg321Player()       # instanciate the player
sonidos= MPyg321Player()


GPIO.setmode(GPIO.BCM)   # Creamos el objeto para GPIO
GPIO.setwarnings(False)  #Oculta los avisos de los GPIO

# GPIO24 boton1 Y 17 boton2 SON LOS PULSADORES
GPIO.setup(24, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(9, GPIO.IN)

# Gpio 18 led1 Y 22 led2 SON LOS LEDS
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

# definimos variables para guardar el estado del led
# por defecto el estado del led es False (apagado)
led18_estado=False
led22_estado=False
led10_estado=False
led25_estado=False

def encender_led(led,estado):
    if estado == False:
        GPIO.output(led, GPIO.HIGH)
        # file = ' subemelaradio.mp3'
        time.sleep(0.3) # sino ponemos un sleep no funciona bien el apagado/encendido
        musica.play_song("subemelaradio.mp3") # play a song
        estado = True  
        return(estado)                      
    else:
        musica.stop()
        GPIO.output(led, GPIO.LOW)
        time.sleep(0.3) # sino ponemos un sleep no funciona bien el apagado/encendido
        estado = False
        return (estado)

while True:
    time.sleep(0.1) # Lo uso para usar menos CPU dentro de un While que siempre se cumple, pasa del 99% al 0,6%
    
    inputValue24 = GPIO.input(24) #Si pulsamos el Botón1
    if inputValue24 == True:
        led18_estado= encender_led(18,led18_estado)

    inputValue17 = GPIO.input(17) # Si pulsamos el Botón2
    if inputValue17 == True:
        led22_estado = encender_led(22,led22_estado)  

    inputValue27 = GPIO.input(27) # Si pulsamos el Botón3
    if inputValue27 == True:
    	led10_estado = encender_led(10,led10_estado)

    inputValue9 = GPIO.input(9) # Si pulsamos el Botón4
    if inputValue9 == True:
    	led25_estado = encender_led(25,led25_estado)

GPIO.cleanup()
