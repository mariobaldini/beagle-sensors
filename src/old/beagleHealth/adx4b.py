# BeagleBone Black Health Sensors
# Autores: Mario Baldini, Joao Baggio, Raimes Moraes


POWER_CTL_addr   = 0x2D;    
DATA_FORMAT_addr = 0x31;



import numpy
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

adx1.write8(POWER_CTL_addr, 0x08)
adx2.write8(POWER_CTL_addr, 0x08)
adx3.write8(POWER_CTL_addr, 0x08)
adx4.write8(POWER_CTL_addr, 0x08)




#D7		D6		D5		D4		D3		D2		D1
#SELF_TEST	SPI		INT_INVERT	FULL_RES	Justify		Range 1		Range 2
#0		1		1		0		0		0		1		#arduino  0x31
#0		0		0		0		0		0		0		#nosso: 2g

adx1.write8(DATA_FORMAT_addr, 0x00)



while True:
	
	t_init = time.time()

	# solicita todos os valores em 1 comando
	# recomendacao do datasheet, para garantir sincronia

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


	acc1X_lb = adx1.readU8(0x32) # 0x32
	acc1X_hb = adx1.readU8(0x33) # 0x33
	acc1Y_lb = adx1.readU8(0x34) # 0x34
	acc1Y_hb = adx1.readU8(0x35) # 0x35
	acc1Z_lb = adx1.readU8(0x36) # 0x36
	acc1Z_hb = adx1.readU8(0x37) # 0x37

	acc1Xb = (acc1X_hb << 8) + acc1X_lb
	acc1Yb = (acc1Y_hb << 8) + acc1Y_lb
	acc1Zb = (acc1Z_hb << 8) + acc1Z_lb

	t_end = (time.time() - t_init) * 1000


	#print '(',acc1X,acc1Y,acc1Z,')\t\t\t(',acc1Xb,acc1Yb,acc1Zb,')'

	print acc1X_lb,acc1X_hb,'\t',acc1Y_lb,acc1Y_hb,'\t',acc1Z_lb,acc1Z_hb


	sleep(0.050)


