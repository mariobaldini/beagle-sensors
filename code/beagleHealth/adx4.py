# BeagleBone Black Health Sensors
# Autores: Mario Baldini, Joao Baggio, Raimes Moraes

import os
import time
import Adafruit_BBIO.ADC as ADC
from time import sleep
from Adafruit_I2C import Adafruit_I2C

ADC.setup()     
adx1 = Adafruit_I2C(0x1d, 1) #(device addr, i2c bus addr)
adx2 = Adafruit_I2C(0x53, 1) 
adx3 = Adafruit_I2C(0x1d, 2) 
adx4 = Adafruit_I2C(0x53, 2) 


POWER_CTL_addr   = 0x2D;    
#DATA_FORMAT_addr = 0x31;

adx1.write8(POWER_CTL_addr, 0x08)
adx2.write8(POWER_CTL_addr, 0x08)
adx3.write8(POWER_CTL_addr, 0x08)
adx4.write8(POWER_CTL_addr, 0x08)


while True:
	
	t_init = time.time()

	# solicita todos os valores em 1 comando
	# recomendacao do datasheet, para garantir sincronia

	#acc1 = adx1.readList(0x32,6)  
	#acc1X_l = acc1[0] # 0x32
	#acc1X_h = acc1[1] # 0x33
	#acc1Y_l = acc1[2] # 0x34
	#acc1Y_h = acc1[3] # 0x35
	#acc1Z_l = acc1[4] # 0x36
	#acc1Z_h = acc1[5] # 0x37
	#acc1X = (acc1X_h << 8) + acc1X_l
	#acc1Y = (acc1Y_h << 8) + acc1Y_l
	#acc1Z = (acc1Z_h << 8) + acc1Z_l



	acc1 = adx1.readList(0x32,6)  
	acc1X_l = acc1[0] # 0x32
	acc1X_h = acc1[1] # 0x33
	acc1Y_l = acc1[2] # 0x34
	acc1Y_h = acc1[3] # 0x35
	acc1Z_l = acc1[4] # 0x36
	acc1Z_h = acc1[5] # 0x37
	acc1X = (acc1X_h << 8) + acc1X_l
	acc1Y = (acc1Y_h << 8) + acc1Y_l
	acc1Z = (acc1Z_h << 8) + acc1Z_l








	acc2 = adx2.readList(0x32,6)  
	acc2X_l = acc2[0] # 0x32
	acc2X_h = acc2[1] # 0x33
	acc2Y_l = acc2[2] # 0x34
	acc2Y_h = acc2[3] # 0x35
	acc2Z_l = acc2[4] # 0x36
	acc2Z_h = acc2[5] # 0x37
	acc2X = (acc2X_h << 8) + acc2X_l
	acc2Y = (acc2Y_h << 8) + acc2Y_l
	acc2Z = (acc2Z_h << 8) + acc2Z_l

	
	acc3 = adx3.readList(0x32,6)
	acc3X_l = acc3[0] # 0x32
	acc3X_h = acc3[1] # 0x33
	acc3Y_l = acc3[2] # 0x34
	acc3Y_h = acc3[3] # 0x35
	acc3Z_l = acc3[4] # 0x36
	acc3Z_h = acc3[5] # 0x37
	acc3X = (acc3X_h << 8) + acc3X_l
	acc3Y = (acc3Y_h << 8) + acc3Y_l
	acc3Z = (acc3Z_h << 8) + acc3Z_l


	acc4 = adx4.readList(0x32,6) 
	acc4X_l = acc4[0] # 0x32
	acc4X_h = acc4[1] # 0x33
	acc4Y_l = acc4[2] # 0x34
	acc4Y_h = acc4[3] # 0x35
	acc4Z_l = acc4[4] # 0x36
	acc4Z_h = acc4[5] # 0x37
	acc4X = (acc4X_h << 8) + acc4X_l
	acc4Y = (acc4Y_h << 8) + acc4Y_l
	acc4Z = (acc4Z_h << 8) + acc4Z_l




	
	p40_raw = ADC.read_raw("P9_40")	
	#p40_norm = ADC.read("P9_40")	
	#print 'ADC P9_40\t Normalizado: ', p40_norm, '\tADC P9_40 RAW: ', p40_raw 


	# Exemplo com SPI
	# from Adafruit_BBIO.SPI import SPI
	# spi = SPI(0,0)
	# spi.readbytes(1)




	t_end = (time.time() - t_init) * 1000



#	print 'ADXL345 (x,y,z):\t', accX, '\t', accY, '\t', accZ, '\tADC_P9_40 (raw):', p40_raw, '\t Elapsed (ms):', t_end 

	#print '(', acc1X, '\t', acc1Y, '\t', acc1Z, ')\t(', acc2X, '\t', acc2Y, '\t', acc2Z, ')\t(', acc3X, '\t', acc3Y, '\t', acc3Z, ')\tElapsed (ms):', t_end 


	print '(',acc1X,acc1Y,acc1Z,')\t\t(',acc2X,acc2Y,acc2Z,')\t\t(',acc3X,acc3Y,acc3Z,')\t\t(',acc4X,acc4Y,acc4Z,')\t\t',t_end 


	#print '1: (',acc1X,acc1Y,acc1Z,')'
	#print '2: (',acc2X,acc2Y,acc2Z,')'
	#print '3: (',acc3X,acc3Y,acc3Z,')'
	#print '4: (',acc4X,acc4Y,acc4Z,')'
	#print 'Elapsed: ',t_end 

	#os.system('clear')

	sleep(0.050)


