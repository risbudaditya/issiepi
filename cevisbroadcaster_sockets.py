import RPi.GPIO as GPIO
import time as time
import socket as socket
import threading

port = 12345

tilt = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(tilt,GPIO.IN)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(),port))
serversocket.listen()

connections = {}

class socketlistener:
	def __init__(self, interval=0.5):
		self.interval = interval
		thread= threading.Thread(target=self.run, args=())
		thread.daemon=True
		thread.start()
	def run(self):
		while True:
			(clientsocket, address) = serversocket.accept()
			connections.update( {clientsocket : address} )
			time.sleep(self.interval)
		
socketlistener = socketlistener();

ping = 1
try:
	while True:
		ping = GPIO.input(tilt)
		time.sleep(0.15)
		if ping == 0:
			print("Ping")
			for clientsocket, value in connections.keys():
				clientsocket.send("Ping")
		else:
			print("No ping")
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
