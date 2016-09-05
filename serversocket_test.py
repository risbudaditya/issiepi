'''
Created on Sep 5, 2016

@author: Aditya
'''
import time as time
import socket as socket
import threading

port = 12345

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
            print ("Got connection from: ", clientsocket, ", address: ", address)
            time.sleep(self.interval)
        
socketlistener = socketlistener();
time.sleep(20)