from machine import Pin, I2C
import ssd1306



i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)


display.fill(0)
display.text('Hello World', 0, 0, 1)
display.show()
count = 0
while True:
    
    while count < 20 :
        display.text("s", count*5, 30, 1)
        display.show()
        count = count+1
    count = 0
    display.fill(0)