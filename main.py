from machine import Pin
from time import sleep

red_led = Pin(25, Pin.OUT)
blue_led = Pin(26, Pin.OUT)
green_led = Pin(33, Pin.OUT)

# -- Allume, attends 0.5s et éteins la led rouge
red_led.on()
sleep(0.5)
red_led.off()

# -- Boucle clignotant avec les 3 couleurs (i = 0.5s)
# while True:
#     red_led.on()
#     blue_led.off()
#     sleep(0.5)
#     red_led.off()
#     blue_led.on()
#     sleep(0.5)


def rgb_(red, green, blue):
    red_led.value(red)
    green_led.value(green)
    blue_led.value(blue)

colors = [(0, 0, 0),
          (1, 0, 0),
          (0, 1, 0),
          (0, 0, 1),
          (1, 0, 1),
          (0, 1, 1),
          (1, 0, 1),
          (0, 0, 0)]

for color in colors:
    rgb_(color[0], color[1], color[2])
    sleep(0.5)