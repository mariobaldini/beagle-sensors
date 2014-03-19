#!/usr/bin/env python


import pylab
from pylab import *
import Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import random


root = Tkinter.Tk()
root.wm_title("Beaglebone Sensors Experiments")

xAchse=pylab.arange(0,100,1)
yAchse=pylab.array([0]*100)

fig = pylab.figure(1)

ax1 = fig.add_subplot(221)
ax1.grid(True)
ax1.set_title("ADXL345 - I2C-1/0x1D")
ax1.set_ylabel("Amplitude (G)")
ax1.axis([0,100,-3,3])
line11=ax1.plot(xAchse,yAchse,'-')
line12=ax1.plot(xAchse,yAchse,'-')
line13=ax1.plot(xAchse,yAchse,'-')

ax2 = fig.add_subplot(222)
ax2.grid(True)
ax2.set_title("ADXL345 - I2C-1/0x53")
ax2.set_ylabel("Amplitude (G)")
ax2.axis([0,100,-3,3])
line21=ax2.plot(xAchse,yAchse,'-')
line22=ax2.plot(xAchse,yAchse,'-')
line23=ax2.plot(xAchse,yAchse,'-')

ax3 = fig.add_subplot(223)
ax3.grid(True)
ax3.set_title("ADXL345 - I2C-2/0x1D")
ax3.set_ylabel("Amplitude (G)")
ax3.axis([0,100,-3,3])
line31=ax3.plot(xAchse,yAchse,'-')
line32=ax3.plot(xAchse,yAchse,'-')
line33=ax3.plot(xAchse,yAchse,'-')

ax4 = fig.add_subplot(224)
ax4.grid(True)
ax4.set_title("ADXL345 - I2C-2/0x53")
ax4.set_ylabel("Amplitude (G)")
ax4.axis([0,100,-3,3])
line41=ax4.plot(xAchse,yAchse,'-')
line42=ax4.plot(xAchse,yAchse,'-')
line43=ax4.plot(xAchse,yAchse,'-')



canvas = FigureCanvasTkAgg(fig, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

#toolbar = NavigationToolbar2TkAgg( canvas, root )
#toolbar.update()
canvas._tkcanvas.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

values11=[]
values11 = [0 for x in range(100)]
values12=[]
values12= [0 for x in range(100)]
values13=[]
values13= [0 for x in range(100)]

values21=[]
values21 = [0 for x in range(100)]
values22=[]
values22= [0 for x in range(100)]
values23=[]
values23= [0 for x in range(100)]

values31=[]
values31 = [0 for x in range(100)]
values32=[]
values32= [0 for x in range(100)]
values33=[]
values33= [0 for x in range(100)]

values41=[]
values41 = [0 for x in range(100)]
values42=[]
values42= [0 for x in range(100)]
values43=[]
values43= [0 for x in range(100)]


def waveformGenerator():
  global values11, values12, values13
  global values21, values22, values23
  global values31, values32, values33
  global values41, values42, values43

  
  next11=random.uniform(-2.0, 2.0) 
  next12=random.uniform(-2.0, 2.0) 
  next13=random.uniform(-2.0, 2.0) 
  next21=random.uniform(-2.0, 2.0) 
  next22=random.uniform(-2.0, 2.0) 
  next23=random.uniform(-2.0, 2.0) 
  next31=random.uniform(-2.0, 2.0) 
  next32=random.uniform(-2.0, 2.0) 
  next33=random.uniform(-2.0, 2.0) 
  next41=random.uniform(-2.0, 2.0) 
  next42=random.uniform(-2.0, 2.0) 
  next43=random.uniform(-2.0, 2.0) 

  print '1:', next11, ',', next12, ',', next13
  print '2:', next21, ',', next22, ',', next23
  print '3:', next31, ',', next32, ',', next33
  print '4:', next41, ',', next42, ',', next43


  values11.append(next11)
  values12.append(next12)
  values13.append(next13)
  values21.append(next21)
  values22.append(next22)
  values23.append(next23)
  values31.append(next31)
  values32.append(next32)
  values33.append(next33)
  values41.append(next41)
  values42.append(next42)
  values43.append(next43)


  root.after(10,waveformGenerator)




def RealtimePloter():
  global wScale
  global values11,values12,values13
  global values21,values22,values23
  global values31,values32,values33
  global values41,values42,values43

  NumberSamples=min(len(values11),wScale.get())
  CurrentXAxis=pylab.arange(len(values11)-NumberSamples,len(values11),1)

  line11[0].set_data(CurrentXAxis,pylab.array(values11[-NumberSamples:]))
  line12[0].set_data(CurrentXAxis,pylab.array(values12[-NumberSamples:]))
  line13[0].set_data(CurrentXAxis,pylab.array(values13[-NumberSamples:]))
  line21[0].set_data(CurrentXAxis,pylab.array(values21[-NumberSamples:]))
  line22[0].set_data(CurrentXAxis,pylab.array(values22[-NumberSamples:]))
  line23[0].set_data(CurrentXAxis,pylab.array(values23[-NumberSamples:]))
  line31[0].set_data(CurrentXAxis,pylab.array(values21[-NumberSamples:]))
  line32[0].set_data(CurrentXAxis,pylab.array(values22[-NumberSamples:]))
  line33[0].set_data(CurrentXAxis,pylab.array(values23[-NumberSamples:]))
  line41[0].set_data(CurrentXAxis,pylab.array(values21[-NumberSamples:]))
  line42[0].set_data(CurrentXAxis,pylab.array(values22[-NumberSamples:]))
  line43[0].set_data(CurrentXAxis,pylab.array(values23[-NumberSamples:]))

  ax1.axis([CurrentXAxis.min(),CurrentXAxis.max(),-3,3])
  ax2.axis([CurrentXAxis.min(),CurrentXAxis.max(),-3,3])
  ax3.axis([CurrentXAxis.min(),CurrentXAxis.max(),-3,3])
  ax4.axis([CurrentXAxis.min(),CurrentXAxis.max(),-3,3])


  canvas.draw()
  root.after(25,RealtimePloter)
  #canvas.draw()

  #manager.show()

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tkinter.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tkinter.BOTTOM)

wScale = Tkinter.Scale(master=root,label="View Width:", from_=3, to=1000,sliderlength=30,length=ax1.get_frame().get_window_extent().width, orient=Tkinter.HORIZONTAL)
wScale.pack(side=Tkinter.BOTTOM)

wScale.set(100)

root.protocol("WM_DELETE_WINDOW", _quit)
root.after(100,waveformGenerator)
root.after(100,RealtimePloter)
Tkinter.mainloop()
pylab.show()