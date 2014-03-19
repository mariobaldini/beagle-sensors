# Require: http://www.pyqtgraph.org/


from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import random
from pyqtgraph.ptime import time

from pyqtgraph import MultiPlotWidget

app = QtGui.QApplication([])
w = pg.GraphicsWindow()
w.setWindowTitle('Beaglebone Health Sensors Experiments')
p1 = w.addPlot(0,0, title="Accelerometer - I2C-1 0x1D  (G)")
p2 = w.addPlot(1,0, title="Accelerometer - I2C-1 0x53  (G)")
p3 = w.addPlot(2,0, title="Accelerometer - I2C-2 0x1D  (G)")
p4 = w.addPlot(3,0, title="Accelerometer - I2C-2 0x1D  (G)")

p1.showGrid(True, True)
p2.showGrid(True, True)
p3.showGrid(True, True)
p4.showGrid(True, True)
w.show()





#QtGui.QApplication.setGraphicsSystem('raster')
##app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)


data_window_size = 500


##p = pg.plot()
##p.setWindowTitle('pyqtgraph example: MultiPlotSpeedTest')


# p.setYRange(-1, 1)
p1.setXRange(0, data_window_size)
# p.resize(600,600)
p1.enableAutoScale()

# p.clear()
# p.plot([0,1,-1], pen='r')




dataX = [random.uniform(-2.0, 2.0) for x in range(10000)]
dataY = [random.uniform(-2.0, 2.0) for x in range(10000)]
dataZ = [random.uniform(-2.0, 2.0) for x in range(10000)]


cX = pg.PlotCurveItem(pen='r')
cX.setPos(0,1)
cY = pg.PlotCurveItem(pen='g')
cY.setPos(0,1)
cZ = pg.PlotCurveItem(pen='b')
cZ.setPos(0,1)


p1.addItem(cX)
p1.addItem(cY)
p1.addItem(cZ)


lastTime = time()
def update():
  global dataX, dataY, dataZ, data_window_size

  dataX.append(random.uniform(-2.0, 2.0))
  dataY.append(random.uniform(-2.0, 2.0))
  dataZ.append(random.uniform(-2.0, 2.0))


  cX.setData(dataX[len(dataX)-data_window_size:len(dataX)])
  cY.setData(dataY[len(dataY)-data_window_size:len(dataY)])
  cZ.setData(dataZ[len(dataZ)-data_window_size:len(dataZ)])
  

  #p.addItem(pg.PlotCurveItem([1,2,1,-1], pen='b'))
  


  global lastTime
  now = time()
  dt = now - lastTime
  lastTime = now
  fps = 1.0/dt
  # p1.setTitle('%0.2f fps' % fps)
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
