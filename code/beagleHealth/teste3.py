# ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

from adxl345 import ADXL345
from time import sleep



adxl345 = ADXL345()
    
axes = adxl345.getAxes(True)
#print "ADXL345 on address 0x%x:" % (adxl345.address)
#print "   x = %.3fG" % ( axes['x'] )
#print "   y = %.3fG" % ( axes['y'] )
#print "   z = %.3fG" % ( axes['z'] )



while True:

	axes = adxl345.getAxes(True)

	print "x: %.5f" % (axes['x']), "y: %.5f" % (axes['y']),  "z: %.5f" % (axes['z'])

#	sleep(0.050)
	sleep(0.100)
