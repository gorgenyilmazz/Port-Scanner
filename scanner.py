#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our Target
if len(sys.argv) == 2:

	#Translate hostname to IPv4 (we can give directly host name)
	target = socket.gethostbyname(sys.argv[1]) 
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Add a banner
print("-" * 50)
print("Scanning target " +target)
print("Time started: " +str(datetime.now()))
print("-" * 50) 

try:
	for port in range(50, 85):
		#Here we made a socket instance and passed it two parameters.
		#AF_INET refers to the addresss family ipv4.
		#SOCK_STREAM means connection oriented TCP protocol or we can say that is port actually
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		#if this cant make a connection in this port then will wait one second and move on
		socket.setdefaulttimeout(1)
		
		#if connection is succesful result = 0 otherwise result = 1
		result = s.connect_ex((target,port)) 
		if result == 0:
			print("Port {} is open".format(port))
		#close connection
		s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to the server.")
	sys.exit() 																

