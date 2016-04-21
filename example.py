from gpiozero import TrafficLights, Button
from time import sleep

tl1 = TrafficLights(13, 19, 26)
tl2 = TrafficLights(21, 20, 16)
tl3 = TrafficLights(10, 9, 11)
tl4 = TrafficLights(7, 8, 25)
cross1 = TrafficLights(2, 3, 4)
cross2 = TrafficLights(18, 15, 14)
btn = Button(5)

def pressed():
    print("Don't push the button!")

btn.when_pressed = pressed

while True:
    tl1.red.on()
    sleep(1)
    tl1.amber.on()
    btn.press() # for demo purposes
    sleep(1)
    tl1.off()
    tl1.green.on()
    sleep(3)
    tl1.off()
    tl1.amber.on()
    sleep(1)
    tl1.off()

while True:
    tl1.value = (1, 0, 0)
    sleep(1)
    tl1.value = (1, 1, 0)
    sleep(1)
    tl1.value = (0, 0, 1)
    sleep(3)
    tl1.value = (0, 1, 0)
    sleep(1)

