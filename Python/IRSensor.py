import time
from machine import Pin,PWM

pwm1=PWM(Pin(0))
pwm1.freq(1000)

pwm2=PWM(Pin(1))
pwm2.freq(1000)

left1=machine.Pin(10,Pin.OUT)
left2=machine.Pin(11,Pin.OUT)
right1=machine.Pin(12,Pin.OUT)
right2=machine.Pin(13,Pin.OUT)

sensorPins=[machine.Pin(pinNumber,machine.Pin.IN) for pinNumber in range(2,10)]

def readRI():
    IR=[]
    for pin in sensorPins:
        IR.append(pin.value())
    return IR

    
while True:    
    IRData = readRI()
    #print(IRData)
    LeftSensors=IRData[4:]
    RightSensors=IRData[:4]
    LeftGain= IRData[4]+IRData[5]+IRData[6]+IRData[7]
    RightGain= IRData[3]+IRData[2]+IRData[1]+IRData[0]

    pwm1.duty_u16(60000-RightGain*15000)
    pwm2.duty_u16(60000-LeftGain*55000)
    
    left1.value(0)
    left2.value(1)
    right1.value(0)
    right2.value(1)


    
    