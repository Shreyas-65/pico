import machine
import utime

led=[]

for i in range(4):
    led.append(machine.Pin(i, machine.Pin.OUT))

sd=0.1
cl=0
lc=4

while True:
    led[cl].value(1)
    pl=(cl-1+lc)%lc
    led[pl].value(0)
    utime.sleep(sd)
    cl=(cl+1)%lc
    
 