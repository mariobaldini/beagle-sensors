# BeagleBone Black Health Sensors
# Autores: Mario Baldini, Joao Baggio, Raimes Moraes


import socket   #for sockets
import sys  #for exit
import string


# Begin network connect
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = 'localhost'
port = 8888
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip
# End network connect





while (True):
	
	reply = s.recv(8192)
	parsed = string.split(reply, ',')
	timestamp = parsed[0]	
	adx1X = parsed[1]
	adx1Y = parsed[2]
	adx1Z = parsed[3]
	adx2X = parsed[4]
	adx2Y = parsed[5]
	adx2Z = parsed[6]
	adx3X = parsed[7]
	adx3Y = parsed[8]
	adx3Z = parsed[9]
	adx4X = parsed[10]
	adx4Y = parsed[11]
	adx4Z = parsed[12]
	p37_raw = parsed[13]
	p38_raw = parsed[14]
	p39_raw = parsed[15]
	p40_raw = parsed[16]



	