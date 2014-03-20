# Require: http://www.pyqtgraph.org/


from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import random
from pyqtgraph.ptime import time
from pyqtgraph import MultiPlotWidget
import socket   #for sockets
import sys  #for exit
import string


app = QtGui.QApplication([])
w = pg.GraphicsWindow()
w.setWindowTitle('Beaglebone Health Sensors Experiments - https://github.com/mariobaldini/beagle-sensors')

adx1 = w.addPlot(0,0, title="Accel.  -  I2C-1 0x1D  -  (X,Y,Z)-(Red,Green,Blue)  -  Unit: G")
adx2 = w.addPlot(1,0, title="Accel.  -  I2C-1 0x1D  -  (X,Y,Z)-(Red,Green,Blue)  -  Unit: G")
adx3 = w.addPlot(2,0, title="Accel.  -  I2C-1 0x1D  -  (X,Y,Z)-(Red,Green,Blue)  -  Unit: G")
adx4 = w.addPlot(3,0, title="Accel.  -  I2C-1 0x1D  -  (X,Y,Z)-(Red,Green,Blue)  -  Unit: G")

ain1 = w.addPlot(0,1, title="Analog Input 0 - Pin 40  (mV)")
ain2 = w.addPlot(1,1, title="Analog Input 1 - Pin 39  (mV)")
ain3 = w.addPlot(2,1, title="Analog Input 2 - Pin 38  (mV)")
ain4 = w.addPlot(3,1, title="Analog Input 3 - Pin 37  (mV)")

adx1.showGrid(True, True)
adx2.showGrid(True, True)
adx3.showGrid(True, True)
adx4.showGrid(True, True)
ain1.showGrid(True, True)
ain2.showGrid(True, True)
ain3.showGrid(True, True)
ain4.showGrid(True, True)

w.show()


#QtGui.QApplication.setGraphicsSystem('raster')
##app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)




##p = pg.plot()
##p.setWindowTitle('pyqtgraph example: MultiPlotSpeedTest')

# p.setYRange(-1, 1)
# adx1.setXRange(0, data_window_size)
# p.resize(600,600)

adx1.enableAutoRange('y', True)
adx2.enableAutoRange('y', True)
adx3.enableAutoRange('y', True)
adx4.enableAutoRange('y', True)

ain1.enableAutoRange('y', True)
ain2.enableAutoRange('y', True)
ain3.enableAutoRange('y', True)
ain4.enableAutoRange('y', True)

# p.clear()
# p.plot([0,1,-1], pen='r')

data_window_size = 500

adx1dataX = [0] * data_window_size
adx1dataY = [0] * data_window_size
adx1dataZ = [0] * data_window_size

adx2dataX = [0] * data_window_size
adx2dataY = [0] * data_window_size
adx2dataZ = [0] * data_window_size

adx3dataX = [0] * data_window_size
adx3dataY = [0] * data_window_size
adx3dataZ = [0] * data_window_size

adx4dataX = [0] * data_window_size
adx4dataY = [0] * data_window_size
adx4dataZ = [0] * data_window_size

ain1data = [0] * data_window_size
ain2data = [0] * data_window_size
ain3data = [0] * data_window_size
ain4data = [0] * data_window_size



adx1cX = pg.PlotCurveItem(pen='r')
# adx1cX.setPos(0,0)
adx1cY = pg.PlotCurveItem(pen='g')
# adx1cY.setPos(0,0)
adx1cZ = pg.PlotCurveItem(pen='b')
# adx1cZ.setPos(0,0)

adx2cX = pg.PlotCurveItem(pen='r')
# adx2cX.setPos(0,1)
adx2cY = pg.PlotCurveItem(pen='g')
# adx2cY.setPos(0,1)
adx2cZ = pg.PlotCurveItem(pen='b')
# adx2cZ.setPos(0,1)

adx3cX = pg.PlotCurveItem(pen='r')
# adx3cX.setPos(0,1)
adx3cY = pg.PlotCurveItem(pen='g')
# adx3cY.setPos(0,1)
adx3cZ = pg.PlotCurveItem(pen='b')
# adx3cZ.setPos(0,1)

adx4cX = pg.PlotCurveItem(pen='r')
# adx4cX.setPos(0,1)
adx4cY = pg.PlotCurveItem(pen='g')
# adx4cY.setPos(0,1)
adx4cZ = pg.PlotCurveItem(pen='b')
# adx4cZ.setPos(0,1)

ain1c = pg.PlotCurveItem(pen='r')
ain2c = pg.PlotCurveItem(pen='g')
ain3c = pg.PlotCurveItem(pen='b')
ain4c = pg.PlotCurveItem(pen='y')



adx1.addItem(adx1cX)
adx1.addItem(adx1cY)
adx1.addItem(adx1cZ)

adx2.addItem(adx2cX)
adx2.addItem(adx2cY)
adx2.addItem(adx2cZ)

adx3.addItem(adx3cX)
adx3.addItem(adx3cY)
adx3.addItem(adx3cZ)

adx4.addItem(adx4cX)
adx4.addItem(adx4cY)
adx4.addItem(adx4cZ)

ain1.addItem(ain1c)
ain2.addItem(ain2c)
ain3.addItem(ain3c)
ain4.addItem(ain4c)




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






lastTime = time()
def update():
  global data_window_size
  global adx1dataX, adx1dataY, adx1dataZ
  global adx2dataX, adx2dataY, adx2dataZ
  global adx3dataX, adx3dataY, adx3dataZ
  global adx4dataX, adx4dataY, adx4dataZ
  global ain1data, ain2data, ain3data, ain4data



  reply = s.recv(4096)
  parsed = string.split(reply, ',')

  timestamp = float(parsed[0])
  adx1X = float(parsed[1])
  adx1Y = float(parsed[2])
  adx1Z = float(parsed[3])
  adx2X = float(parsed[4])
  adx2Y = float(parsed[5])
  adx2Z = float(parsed[6])
  adx3X = float(parsed[7])
  adx3Y = float(parsed[8])
  adx3Z = float(parsed[9])
  adx4X = float(parsed[10])
  adx4Y = float(parsed[11])
  adx4Z = float(parsed[12])
  p37_raw = float(parsed[13])
  p38_raw = float(parsed[14])
  p39_raw = float(parsed[15])
  p40_raw = float(parsed[16])


  adx1dataX.append(adx1X)
  adx1dataY.append(adx1Y)
  adx1dataZ.append(adx1Z)

  adx2dataX.append(adx2X)
  adx2dataY.append(adx2Y)
  adx2dataZ.append(adx2Z)

  adx3dataX.append(adx3X)
  adx3dataY.append(adx3Y)
  adx3dataZ.append(adx3Z)

  adx4dataX.append(adx4X)
  adx4dataY.append(adx4Y)
  adx4dataZ.append(adx4Z)

  ain1data.append(p40_raw)
  ain2data.append(p39_raw)
  ain3data.append(p38_raw)
  ain4data.append(p37_raw)


  # adx1dataX.append(random.uniform(-2.0, 2.0))
  # adx1dataY.append(random.uniform(-2.0, 2.0))
  # adx1dataZ.append(random.uniform(-2.0, 2.0))

  # adx2dataX.append(random.uniform(-2.0, 2.0))
  # adx2dataY.append(random.uniform(-2.0, 2.0))
  # adx2dataZ.append(random.uniform(-2.0, 2.0))

  # adx3dataX.append(random.uniform(-2.0, 2.0))
  # adx3dataY.append(random.uniform(-2.0, 2.0))
  # adx3dataZ.append(random.uniform(-2.0, 2.0))

  # adx4dataX.append(random.uniform(-2.0, 2.0))
  # adx4dataY.append(random.uniform(-2.0, 2.0))
  # adx4dataZ.append(random.uniform(-2.0, 2.0))


  # ain1data.append(random.uniform(0, 1800))
  # ain2data.append(random.uniform(0, 1800))
  # ain3data.append(random.uniform(0, 1800))
  # ain4data.append(random.uniform(0, 1800))



  adx1cX.setData(adx1dataX[len(adx1dataX)-data_window_size:len(adx1dataX)])
  adx1cY.setData(adx1dataY[len(adx1dataY)-data_window_size:len(adx1dataY)])
  adx1cZ.setData(adx1dataZ[len(adx1dataZ)-data_window_size:len(adx1dataZ)])
  
  adx2cX.setData(adx2dataX[len(adx2dataX)-data_window_size:len(adx2dataX)])
  adx2cY.setData(adx2dataY[len(adx2dataY)-data_window_size:len(adx2dataY)])
  adx2cZ.setData(adx2dataZ[len(adx2dataZ)-data_window_size:len(adx2dataZ)])
  
  adx3cX.setData(adx3dataX[len(adx3dataX)-data_window_size:len(adx3dataX)])
  adx3cY.setData(adx3dataY[len(adx3dataY)-data_window_size:len(adx3dataY)])
  adx3cZ.setData(adx3dataZ[len(adx3dataZ)-data_window_size:len(adx3dataZ)])
  
  adx4cX.setData(adx4dataX[len(adx4dataX)-data_window_size:len(adx4dataX)])
  adx4cY.setData(adx4dataY[len(adx4dataY)-data_window_size:len(adx4dataY)])
  adx4cZ.setData(adx4dataZ[len(adx4dataZ)-data_window_size:len(adx4dataZ)])

  ain1c.setData(ain1data[len(ain1data)-data_window_size:len(ain1data)])
  ain2c.setData(ain2data[len(ain2data)-data_window_size:len(ain2data)])
  ain3c.setData(ain3data[len(ain3data)-data_window_size:len(ain3data)])
  ain4c.setData(ain4data[len(ain4data)-data_window_size:len(ain4data)])
  


  # # Update chart titles with current value
  # adx1.setTitle("Accel.  -  I2C-1 0x1D  -  (X,Y,Z)-(Red,Green,Blue)  -  Unit: G")
  # adx2.setTitle("Accel.  -  I2C-1 0x1D  -  (X,Y,Z)-(Red,Green,Blue)  -  Unit: G")
  # adx3.setTitle("Accel.  -  I2C-1 0x1D  -  (X,Y,Z)-(Red,Green,Blue)  -  Unit: G")
  # adx4.setTitle("Accel.  -  I2C-1 0x1D  -  (X,Y,Z)-(Red,Green,Blue)  -  Unit: G")

  # ain1.setTitle("Analog Input 3 - P9-37 - %0.2f (mV)" % p37_raw)
  # ain2.setTitle("Analog Input 2 - P9-38 - %0.2f (mV)" % p38_raw)
  # ain3.setTitle("Analog Input 1 - P9-39 - %0.2f (mV)" % p39_raw)
  # ain4.setTitle("Analog Input 0 - P9-40 - %0.2f (mV)" % p40_raw)






  global lastTime
  now = time()
  dt = now - lastTime
  lastTime = now
  fps = 1.0/dt
  # adx1.setTitle('%0.2f fps' % fps)
  # w.setWindowTitle('%0.2f fps' % fps)
  print fps



timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(5)



## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
