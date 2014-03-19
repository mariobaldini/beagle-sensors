# Require: http://www.pyqtgraph.org/


from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import random
from pyqtgraph.ptime import time

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

p = pg.plot()
p.setWindowTitle('pyqtgraph example: MultiPlotSpeedTest')

data_window_size = 500

p.setYRange(-1, 1)
p.setXRange(0, data_window_size)
# p.resize(600,600)
p.enableAutoScale()

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


p.addItem(cX)
p.addItem(cY)
p.addItem(cZ)


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
  p.setTitle('%0.2f fps' % fps)



timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(5)



## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
