#!/usr/bin/python           

import socket               
import sys
import os
def tester(argument):
    thinker={
            1="Stone",
            2="Paper",
            3="Scissor"
            }
    print thinker.get(argument,"Invalid Choice")
score1=0
s = socket.socket()
score=0
host = input("Enter the hostname for the server you want to connect to: ") 
port = 12345
def printer():
    print("Your Score is ",score1,"Player Score is ",score)
    print("You chose ",turn,"Player chose ",rets)
    s.send("Your Score ",score)
s.connect((host, port))
print s.recv(1024)
os.system("sleep 3s")
print s.recv(1024)
os.system("sleep 2s")
rounds=s.recv(1024)
print ("The number of rounds are: ",rounds)
for i in range(1:range+1):
    turn=input("Enter your choice 1: Stone 2: Paper 3: Scissor")
    rets=s.recv(1024)
    if(rets=="Stone" and turn=="Stone"):
        score=score+0
        printer()
    elif(rets=="Paper" and turn=="Paper"):
        score=score+0
        printer()
    elif(rets=="Scissor" and turn=="Scissor"):
        score=score+0
        printer()
    elif(rets=="Stone" and turn=="Paper"):
        score1=score1+10
        printer()
    elif(rets=="Paper" and turn=="Stone"):
        score=score+10
        printer()
    elif(rets=="Stone" and turn=="Scissor"):
        score=score+10
        printer()
    elif(rets=="Scissor" and turn=="Stone"):
        score1=score1+10
        printer()
    elif(rets=="Paper" and turn=="Scissor"):
        score1=score1+10
        printer()
    elif(rets=="Scissor" and turn=="Paper"):
        score=score+10

s.close()
