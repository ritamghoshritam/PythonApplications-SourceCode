#!/usr/bin/python           

import socket               
import os
import sys
def tester(argument):
    thinker={
            1="Stone",
            2="Paper",
            3="Scissor"
            }
    print thinker.get(argument,"Invalid Choice")
s = socket.socket()         
host = socket.gethostname()
port = 12345            
s.bind((host, port))        

s.listen(5)                 
while True:
   c, addr = s.accept()     
   print ("The server is running on",addr)
   print 'Got connection from', addr
   c.send('Hello client this is the message from the game server so lets start playing!!')
   c.send("\nSo lets start the game")
   os.system("sleep 3s")
   c.send("This is the game of stone paper scissor MY WAY!!")
   os.system("sleep 2s")
   gameplay=input("Enter the number of rounds you want to play...")
   print ("The client is now engaged and the game has already started")
   for i in range(1:gameplay+1):
       turn=input("Enter your choice: 1: Stone 2: Paper 3: Scissor")
       c.send(tester(turn))
       c.recv(1024)
   c.close()        
