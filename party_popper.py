from picozero import RGBLED, Speaker, Switch
from time import sleep

rgb = RGBLED (red=1, green=2, blue=3)
pull = Switch(18)
speaker = Speaker(5)

def pop():
    print('Pop')
  #  rgb.color = (r, g, b)
    speaker.play(262, 0.1)
    rgb.color = (100, 100, 100) 
    sleep(0.1)
    rgb.color = (255, 150, 0) 
    speaker.play(262, 0.6)
    rgb.off()

pull.when_opened = pop
    
#for r in range(0,255,10):
 #   for g in range(0,255,10):
  #      for b in range(0,255,10):
   #         pop(r,g,b)
#rgb.off()   
#pop(255,0,50)