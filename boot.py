# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
#esp.osdebug(None)

import gc
gc.collect()

ssid = 'halsolomax'
password = '1963196319'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(16, Pin.OUT)