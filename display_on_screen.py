from machine import Pin, I2C
from lib.ssd1306 import SSD1306_I2C
import time
import dotenv


i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)

oled = SSD1306_I2C(128, 32, i2c)

number = 21

oled.fill(0)
oled.text("Hello", 0, 0)
oled.text("Number" + str(number), 10, 10)
oled.show()
