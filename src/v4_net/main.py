# BeagleBone Black Health Sensors
# Autores: Mario Baldini, Joao Baggio, Raimes Moraes

import smbus
from time import sleep
import sys
import os
sys.dont_write_bytecode = True   # prevents older pythons generation of compiled .pyc bytecodes in the tree


import driver_adxl345_bus1 as ADXL345_bus1
import driver_adxl345_bus2 as ADXL345_bus2
import Adafruit_BBIO.ADC as ADC

 
## BEGIN
ADC.setup()  


# For cape with 4 ADX
adx1 = ADXL345_bus1.new(1,   0x1D) #adxl345_bus1_add53
adx2 = ADXL345_bus1.new(1,   0x53) #adxl345_bus1_add53
adx3 = ADXL345_bus2.new(2,   0x1D) #adxl345_bus1_add53
adx4 = ADXL345_bus2.new(2,   0x53) #adxl345_bus1_add53 


print "Column 1-3:\tADXL 345, I2C Bus: 1, Address 0x53; Format: x,y,z; +/-0.000 G"
print "Column 4-6:\tADXL 345, I2C Bus: 1, Address 0xXX; Format: x,y,z; +/-0.000 G"
print "Column 7-9:\tADXL 345, I2C Bus: 2, Address 0x53; Format: x,y,z; +/-0.000 G"
print "Column 10-12:\tADXL 345, I2C Bus: 2, Address 0xXX; Format: x,y,z; +/-0.000 G"
print "Column 13-18:\tAnalog inputs. P9_35 - P9_40. mV"
print "---------------------------------------------------------------------"


axes1 = { 'x':0 , 'y':0, 'z':0 }
axes2 = { 'x':0 , 'y':0, 'z':0 }
axes3 = { 'x':0 , 'y':0, 'z':0 }
axes4 = { 'x':0 , 'y':0, 'z':0 }


f = open('output.txt','w')
f.write("Column 1-3:\tADXL 345, I2C Bus: 1, Address 0x53; Format: x,y,z; +/-0.000 G\n")
f.write("Column 4-6:\tADXL 345, I2C Bus: 1, Address 0xXX; Format: x,y,z; +/-0.000 G\n")
f.write("Column 7-9:\tADXL 345, I2C Bus: 2, Address 0x53; Format: x,y,z; +/-0.000 G\n")
f.write("Column 10-12:\tADXL 345, I2C Bus: 2, Address 0xXX; Format: x,y,z; +/-0.000 G\n")
f.write("Column 13-18:\tAnalog inputs. P9_35 - P9_40. mV\n")
f.write("---------------------------------------------------------------------\n")



import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
#wait to accept a connection - blocking call
#conn, addr = s.accept()
 
#display client information
#print 'Connected with ' + addr[0] + ':' + str(addr[1])


csv = ""



while (True):
    


    axes1 = adx1.getAxes(True)
    axes2 = adx2.getAxes(True)
    axes3 = adx3.getAxes(True)
    axes4 = adx4.getAxes(True)



    p35_raw = ADC.read_raw("P9_35")
    p36_raw = ADC.read_raw("P9_36")	
    p37_raw = ADC.read_raw("P9_37")	
    p38_raw = ADC.read_raw("P9_38")	
    p39_raw = ADC.read_raw("P9_39")	
    p40_raw = ADC.read_raw("P9_40")	
	

    sys.stdout.write("%.3f," % ( axes1['x'] ))
    sys.stdout.write("%.3f," % ( axes1['y'] ))
    sys.stdout.write("%.3f," % ( axes1['z'] ))
    sys.stdout.write("\t")
    sys.stdout.write("%.3f," % ( axes2['x'] ))
    sys.stdout.write("%.3f," % ( axes2['y'] ))
    sys.stdout.write("%.3f," % ( axes2['z'] ))
    sys.stdout.write("\t")
    sys.stdout.write("%.3f," % ( axes3['x'] ))
    sys.stdout.write("%.3f," % ( axes3['y'] ))
    sys.stdout.write("%.3f," % ( axes3['z'] ))
    sys.stdout.write("\t")
    sys.stdout.write("%.3f," % ( axes4['x'] ))
    sys.stdout.write("%.3f," % ( axes4['y'] ))
    sys.stdout.write("%.3f," % ( axes4['z'] ))
    sys.stdout.write("\t")
    sys.stdout.write("%07.2f," % ( p35_raw ))
    sys.stdout.write("%07.2f," % ( p36_raw ))
    sys.stdout.write("%07.2f," % ( p37_raw ))
    sys.stdout.write("%07.2f," % ( p38_raw ))
    sys.stdout.write("%07.2f," % ( p39_raw ))
    sys.stdout.write("%07.2f" % ( p40_raw ))


    sys.stdout.write("\n")
    sys.stdout.flush()

    csv = axes1 + "," + axes1
    print csv


    sleep (0.150)  # ms

f.close()






