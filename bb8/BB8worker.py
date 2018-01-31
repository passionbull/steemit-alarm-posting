from bluepy import btle
import struct
import time
import BB8_driver
import sys

def alarm():
	speed = 20
	bb8 = BB8_driver.Sphero()
	bb8.connect()
	bb8.start()
	bb8.roll(speed, 40, 1, False)
	bb8.set_rgb_led(255,0,0,0,False)
	time.sleep(1)
	bb8.set_rgb_led(0,255,0,0,False)
	time.sleep(1)
	bb8.roll(speed, 320, 1, False)
	bb8.set_rgb_led(0,255,255,0,False)
	time.sleep(1)
	bb8.set_rgb_led(255,0,0,0,False)
	time.sleep(1)
	bb8.set_rgb_led(0,255,0,0,False)
	bb8.roll(speed, 0, 1, False)
	time.sleep(1)
	bb8.join()
	bb8.disconnect()

alarm()
