
import time
import Adafruit_BBIO.ADC as ADC
from time import sleep

ADC.setup() 

while True:
	

	p40_raw = ADC.read_raw("P9_40")	
	p40_norm = ADC.read("P9_40")	
	print 'ADC P9_40 RAW: ', p40_raw, '\t\tADC P9_40 Normalizado: %.10f' % p40_norm

	sleep(0.050)


