'''
Created on Sep 5, 2016

@author: Aditya
'''
import unittest
import socket

class Test(unittest.TestCase):

  
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        port = 12345
        destination = 'localhost'
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((destination, port), )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()