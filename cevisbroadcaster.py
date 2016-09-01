import RPi.GPIO as GPIO
import time as time
tilt = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(tilt,GPIO.IN)
ping = 1
try:
	while True:
		ping = GPIO.input(tilt)
		time.sleep(0.15)
		if ping == 0:
			print("Ping")
		else:
			print("No ping")
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
