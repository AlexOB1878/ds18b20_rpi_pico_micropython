from machine import Pin,I2C
import onewire, ds18x20
from i2c_lcd import I2cLcd
import time
import utime
  
#remember to set correct address, possibly 0x27???  
# DEFAULT_I2C_ADDR = 0x3f
DEFAULT_I2C_ADDR = 0x27

#remember for scl and sda to use correct pins or change these values below
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)

# if you have a smaller 16x2 screen use the one below
# lcd = I2cLcd(i2c ,DEFAULT_I2C_ADDR,2,16)
lcd = I2cLcd(i2c ,DEFAULT_I2C_ADDR,4,20)
lcd.move_to(0,0)
lcd.putstr("Outside Temp is")
utime.sleep_ms(3000)

# to create new lines of text on board
lcd.move_to(7,3)
lcd.putstr("test")
utime.sleep_ms(3000)

# pin 15 for the ds18b20 sensor
oneWireBus = ds18x20.DS18X20(onewire.OneWire(Pin(15)))
 
sensors = oneWireBus.scan()
if (len(sensors)==0):
    print('DS18x20 device not found')
else: 
    while True:
        oneWireBus.convert_temp()
        time.sleep_ms(750)
        for s in sensors:
            temp  = oneWireBus.read_temp(s)
            print(temp)
            lcd.move_to(5,1)
            lcd.putstr("{0:.1f} C".format(temp))
        time.sleep_ms(500)


