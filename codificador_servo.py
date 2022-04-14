from machine import Pin, PWM
from time import sleep

SW = Pin(15, Pin.IN, Pin.PULL_UP)
DT = Pin(14, Pin.IN)      # encoder sin módulo Pin(14, Pin.IN, Pin.PULL_UP)
CLK  = Pin(13, Pin.IN)    # encoder sin módulo Pin(13, Pin.IN, Pin.PULL_UP)

servo = PWM(Pin(12))
servo.freq(50)

valor_anterior = True
switch_presionado = False

valor_servo = 4586  # inicial a 90 grados
incremento = 364    # 10 grados
servo.duty_u16(valor_servo)

while True:
     if valor_anterior != CLK.value():
         if CLK.value() == False:
             if DT.value() == False:
                 print("horario")
                 valor_servo = valor_servo - incremento
                 if valor_servo < 1311:     # 180 grados
                    valor_servo = 1311
                 servo.duty_u16(valor_servo)
                 sleep(0.2)
             else:
                 print("antihorario")
                 valor_servo = valor_servo + incremento
                 if valor_servo > 7862:    # 0 grados
                    valor_servo = 7862
                 servo.duty_u16(valor_servo)
                 sleep(0.2)
         valor_anterior = CLK.value()   
    
     if SW.value() == False and not switch_presionado:
         print("SW presionado")
         valor_servo = 4586                # 90 grados
         servo.duty_u16(valor_servo)
         switch_presionado = True
     if SW.value() == True and switch_presionado:
         switch_presionado = False
