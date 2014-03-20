# BeagleBone Black Health Sensors
# Autores: Mario Baldini, Joao Baggio, Raimes Moraes

from time import sleep
import sys
import os
import random
import time
#import smbus
sys.dont_write_bytecode = True   # prevents older pythons generation of compiled .pyc bytecodes in the tree


# import driver_adxl345_bus1 as ADXL345_bus1
# import driver_adxl345_bus2 as ADXL345_bus2
# import Adafruit_BBIO.ADC as ADC

 
## BEGIN
# ADC.setup()  


# For cape with 4 ADX
# adx1 = ADXL345_bus1.new(1,   0x1D) #adxl345_bus1_add53
# adx2 = ADXL345_bus1.new(1,   0x53) #adxl345_bus1_add53
# adx3 = ADXL345_bus2.new(2,   0x1D) #adxl345_bus1_add53
# adx4 = ADXL345_bus2.new(2,   0x53) #adxl345_bus1_add53 


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
 

while (True): 

    #wait to accept a connection - blocking call
    print "Waiting for connections..."
    conn, addr = s.accept()
     
    #display client information
    print 'Connected with ' + addr[0] + ':' + str(addr[1])


    while (True):
        
        timestamp = time.time()

        axes1['x'] = random.uniform(-2.0, 2.0)
        axes1['y'] = random.uniform(-2.0, 2.0)
        axes1['z'] = random.uniform(-2.0, 2.0)

        axes2['x'] = random.uniform(-2.0, 2.0)
        axes2['y'] = random.uniform(-2.0, 2.0)
        axes2['z'] = random.uniform(-2.0, 2.0)

        axes3['x'] = random.uniform(-2.0, 2.0)
        axes3['y'] = random.uniform(-2.0, 2.0)
        axes3['z'] = random.uniform(-2.0, 2.0)

        axes4['x'] = random.uniform(-2.0, 2.0)
        axes4['y'] = random.uniform(-2.0, 2.0)
        axes4['z'] = random.uniform(-2.0, 2.0)

        p37_raw = random.uniform(0, 1800)
        p38_raw = random.uniform(0, 1800)
        p39_raw = random.uniform(0, 1800)
        p40_raw = random.uniform(0, 1800)


        csv = str(timestamp) + ','
        # csv = ''
        csv = csv + str(axes1['x']) + ',' + str(axes1['y']) + ',' + str(axes1['z']) + ',' 
        csv = csv + str(axes2['x']) + ',' + str(axes2['y']) + ',' + str(axes2['z']) + ',' 
        csv = csv + str(axes3['x']) + ',' + str(axes3['y']) + ',' + str(axes3['z']) + ',' 
        csv = csv + str(axes4['x']) + ',' + str(axes4['y']) + ',' + str(axes4['z']) + ',' 
        csv = csv + str(p37_raw) + ',' + str(p38_raw) + ',' + str(p39_raw) + ',' + str(p40_raw) + ','



        try:
            conn.send(csv)
            print csv
        except:
            print('Error sending data over network')
            break
        
        sleep (0.100)  # ms










print 'soft end - no errors'
f.close()






