# BeagleBone Black Health Sensors
# Autores: Mario Baldini, Joao Baggio, Raimes Moraes


import smbus
from time import sleep
import sys
sys.dont_write_bytecode = True   # prevents older pythons generation of compiled .pyc bytecodes in the tree


import driver_adxl345_bus1 as ADXL345_bus1
#import driver_adxl345_bus2 as ADXL345_bus2
import Adafruit_BBIO.ADC as ADC

 
ADC.setup()  
p40_raw = ADC.read_raw("P9_40")	


## BEGIN

# For single ADX connection
adx1 = ADXL345_bus1.new(1,   0x53) #adxl345_bus1_add53
adx2 = adx1
adx3 = adx1
adx4 = adx1

# For cape with 4 ADX
# adx1 = ADXL345_bus1.new(1,   0x1D) #adxl345_bus1_add53
# adx2 = ADXL345_bus1.new(1,   0x53) #adxl345_bus1_add53
# adx3 = ADXL345_bus2.new(2,   0x1D) #adxl345_bus1_add53
# adx4 = ADXL345_bus2.new(2,   0x53) #adxl345_bus1_add53 


print "Column 1-3:\tADXL 345, I2C Bus: 1, Address 0x53; Format: x,y,z; +/-0.000 G"
print "Column 4-6:\tADXL 345, I2C Bus: 1, Address 0xXX; Format: x,y,z; +/-0.000 G"
print "Column 7-9:\tADXL 345, I2C Bus: 2, Address 0x53; Format: x,y,z; +/-0.000 G"
print "Column 10-12:\tADXL 345, I2C Bus: 2, Address 0xXX; Format: x,y,z; +/-0.000 G"



axes1 = { 'x':0 , 'y':0, 'z':0 }
axes2 = { 'x':0 , 'y':0, 'z':0 }
axes3 = { 'x':0 , 'y':0, 'z':0 }
axes4 = { 'x':0 , 'y':0, 'z':0 }


while (True):
    
    
#    print "%.3f" % ( axes['x'] ), "%.3f" % ( axes['y'] ), "%.3f" % ( axes['z'] )


    #axes1 = adx1.getAxes(True)
    axes1 = adx1.getAxes(True)
    axes2 = adx2.getAxes(True)
    axes3 = adx3.getAxes(True)
    axes4 = adx4.getAxes(True)

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
    sys.stdout.write("%.3f," % ( p40_raw ))


    sys.stdout.write("\n")
    sys.stdout.flush()

    sleep (0.150)  # ms








