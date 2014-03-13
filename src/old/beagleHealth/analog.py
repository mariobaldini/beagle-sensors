# BeagleBone Black Health Sensors
# Autores: Mario Baldini, Joao Baggio, Raimes Moraes


import time
import Adafruit_BBIO.ADC as ADC
from time import sleep
from Adafruit_I2C import Adafruit_I2C

ADC.setup()     
adxl345 = Adafruit_I2C(0x53, 2) #(device addr, i2c bus addr)

POWER_CTL_addr   = 0x2D;    
DATA_FORMAT_addr = 0x31;

adxl345.write8(POWER_CTL_addr, 0x08)
adxl345.write8(DATA_FORMAT_addr, 0x01)

while True:
	
	t_init = time.time()

	# solicita todos os valores em 1 comando
	# recomendacao do datasheet, para garantir sincronia
	acc = adxl345.readList(0x32,6)  
	
	accX_l = acc[0] # 0x32
	accX_h = acc[1] # 0x33
	accY_l = acc[2] # 0x34
	accY_h = acc[3] # 0x35
	accZ_l = acc[4] # 0x36
	accZ_h = acc[5] # 0x37

	accX = (accX_h << 8) + accX_l
	accY = (accY_h << 8) + accY_l
	accZ = (accZ_h << 8) + accZ_l

	
	p40_raw = ADC.read_raw("P9_40")	
	#p40_norm = ADC.read("P9_40")	
	#print 'ADC P9_40\t Normalizado: ', p40_norm, '\tADC P9_40 RAW: ', p40_raw 


	# Exemplo com SPI
	# from Adafruit_BBIO.SPI import SPI
	# spi = SPI(0,0)
	# spi.readbytes(1)




	t_end = (time.time() - t_init) * 1000



	print 'ADXL345 (x,y,z):\t', accX, '\t', accY, '\t', accZ, '\tADC_P9_40 (raw):', p40_raw, '\t Elapsed (ms):', t_end  

	sleep(0.050)


