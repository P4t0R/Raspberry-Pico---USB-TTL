from machine import Pin, UART
from time import sleep

led = Pin(25,Pin.OUT)    #Led fisico de Rapsberry pico
uart = UART(1, 9600)     #Configuramos puerto uart

#Variables auxiliares
cnt=1       
msj = None
c=0

#Enviamos mensajes de inicio por uart
uart.write("\t##### Conexión Serial #####\r\n\n")
uart.write("""Escriba un mensaje y este será retornado por
            \rRaspberry Pico, indicando cantidad de caracteres
            \ry el mensaje, de la forma --> b'mensaje'.\r\n\n""")

#Programa principal
while True:
    if uart.any() > 0:           #Si la condición se cumple existe msj
        led.toggle()             #Enciende led al tipear msj
        sleep(5)                 #Tiempo de espera tipeo
        c = uart.any()           #Cantidad de caracteres del msj
        msj = uart.readline()    #La variable msj contiene el mensaje

    if msj != None:              #Condición para saber si es que existe un msj 
        led.toggle()             #Apaga el led
        print("{}.- MSJ {} Caracteres --> {}".format(cnt,c,msj))   #Imprime msj en Thonny
        uart.write("{}.- MSJ {} Caracteres --> {}\r\n".format(cnt,c,msj))    #Envia msj por uart
        msj = None               #Borramos el msj anterior
        cnt+=1   