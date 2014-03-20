# Require: http://www.pyqtgraph.org/


from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsWindow(title="Plot auto-range examples")
win.resize(800,600)
win.setWindowTitle('pyqtgraph example: PlotAutoRange')


p2 = win.addPlot(title="Auto Pan Only")
p2.setAutoPan(y=True)
p2.enableAutoRange(y=True)
curve = p2.plot()


def update():
    
    data = np.ones(100) 
        
    global curve
    #curve.setData(data)

   # global p2
   # p2.plot(1)
   # p2.plot(3)
   # p2.plot(5)



p2.addItem(pg.PlotCurveItem([10,20,40,80,40,20], pen='b'))
    
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(100)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

