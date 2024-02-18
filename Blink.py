import machine
import utime
led_external=machine.Pin(15, machine.Pin.OUT)

led_external.value(0)                                       
utime.sleep(2)
gap=5

while True:
    led_external.toggle()
    utime.sleep(gap)
    gap=gap-0.5
    
    if gap==0:
        gap=5