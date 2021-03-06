from machine import Pin
from time import sleep

SW = Pin(15, Pin.IN, Pin.PULL_UP)
DT = Pin(14, Pin.IN)      # encoder sin módulo Pin(14, Pin.IN, Pin.PULL_UP)
CLK  = Pin(13, Pin.IN)    # encoder sin módulo Pin(13, Pin.IN, Pin.PULL_UP)

valor_anterior = True
switch_presionado = False

while True:
     if valor_anterior != CLK.value():
         if CLK.value() == False:
             if DT.value() == False:
                 print("horario")
                 sleep(0.2)
             else:
                 print("antihorario")
                 sleep(0.2)
         valor_anterior = CLK.value()   
    
     if SW.value() == False and not switch_presionado:
         print("SW presionado") 
         switch_presionado = True
     if SW.value() == True and switch_presionado:
         switch_presionado = False
