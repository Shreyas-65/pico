import machine
import utime

led=[]

for i in range(10,14):
    led.append(machine.Pin(i, machine.Pin.OUT))

button_1 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_2 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_3 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)

sd=0.1
cl=0
lc=4

def action_1():
    global cl,sd,lc
    utime.sleep(0.1)
    led[cl].value(1)
    pl=(cl-1+lc)%lc
    led[pl].value(0)
    cl=(cl+1)%lc
    
def action_2():
    global lc
    
    for i in range (0,lc):
        led[i].value(1)
    utime.sleep(0.5)
    for i in range (0,lc):
        led[i].value(0)
    utime.sleep(0.1)
    
def action_3():
       led[0].value(1)
       led[2].value(1)
        
       utime.sleep(0.5)
            
       led[0].value(0)
       led[2].value(0)
       led[1].value(1)
       led[3].value(1)
       utime.sleep(0.5)
       led[1].value(0)
       led[3].value(0)

action=0

while True:
    print (button_1.value(), action)
    if button_1.value() == 1:
        action = 1
    elif button_2.value() == 1:
        action = 2
        utime.sleep(sd)
    elif button_3.value() == 1:
        action = 3
        
    if action == 1:
        action_1()
    elif action == 2:
        action_2()
        
    elif action == 3:
        action_3()
     