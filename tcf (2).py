#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time
RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(2, RPi.GPIO.OUT)
pwm = RPi.GPIO.PWM(2,100)
RPi.GPIO.setwarnings(False)


speed = 0
prv_temp = 0

try:


		while True:
		
				tmpFile = open( '/sys/class/thermal/thermal_zone0/temp' )
				cpu_temp = int(tmpFile.read())
				tmpFile.close()
				if cpu_temp>=34500 :
				
						if prv_temp<34500 :
						#启动时防止风扇卡死先全功率转0.1秒
								pwm.start(0)
								pwm.ChangeDutyCycle(100)
								time.sleep(.1)
						speed = min( cpu_temp/125-257 , 100 )
						pwm.ChangeDutyCycle(speed)
				else :
						pwm.stop()
				prv_temp = cpu_temp
				
				time.sleep(5)
				
except KeyboardInterrupt:
		pass
pwm.stop()