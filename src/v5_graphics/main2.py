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

nSamples = 500

p.setYRange(-3, 3)
p.setXRange(0, nSamples)
p.resize(600,600)

p.clear()
p.plot([0,1,-1], pen='r')




data = [random.uniform(-2.0, 2.0) for x in range(10000)]

data_window = data[len(data)-100:len(data)] 
print data_window


lastTime = time()
def update():
  global data
  
  # data.append(random.uniform(-2.0, 2.0))
  # data_window = data[len(data)-100:len(data)] 
  # p.plot(data_window, pen='r')
  

  p.addItem(pg.PlotCurveItem([1,2,1,-1], pen='b'))



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
