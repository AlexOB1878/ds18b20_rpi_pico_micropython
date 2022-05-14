from machine import Pin,I2C
import onewire, ds18x20
from i2c_lcd import I2cLcd
import time
import utime
  
DEFAULT_I2C_ADDR = 0x3f

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
lcd = I2cLcd(i2c ,DEFAULT_I2C_ADDR,2,16)
lcd.move_to(0,0)
lcd.putstr("18B20 Demo")
utime.sleep_ms(3000)

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

