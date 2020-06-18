
## BeagleBone Black Framework for Physiological Data Acquisition

Academic reserch project

### Hardware:  
- Beaglebone Black
- Accelerometer (ADXL 345)
- Air flow sensor

### Software:   
- Archlinux
- ic2tools (general i2c tools)
- Python (for raw sensor access)
- X11 / Openbox (for graphical display)


### Data Input/Output Options:  
- Serial connect (Header pin or USB serial)
- Standard HDMI video + mouse + keyboard
- SSH (text mode and graphical, through -X option)

**Sample output:**
```
0.0,0.0,0.0    0.0,0.0,0.0    0.0,0.0,0.0    0.0,0.0,0.0    0.0    0.0    0.0    0.0
```
4x ADXL345 accelerometers and 4x Analog pins. 


#### Feature map
- CSV output to file.
- Graphical User Interface for realtime ploting.
- Dynamic DNS for easier network access
- Clean openbox right click menu
- Customize openbox right click to call functions of the system
- Linux Device Drivers for abstracted access of the hardware?
- Improve syncronization techniques of data sampling (hardware interrupt?)
- MOSH support
- GUI access over network
- Cape design, with generic connectors. (P2 ?)
- Filesystem improvements (to avoid dirty state on sequencial hard power offs)
- Automatic detection and identification of connected sensors.
- Emulated device drivers with file IO (enabling development of custom code without the actual hardware; reading from sample data file and allowing instant switch to real hardware acquisition).


### Installation guide


Requirement: a linux machine to create the SDcard using this guide. Beaglebone documentation also describe how to create using Windows)


- Flash Archlinux to a sdcard: 
http://archlinuxarm.org/platforms/armv7/ti/beaglebone-black

- Update de system: 
`pacman -Syu` 

- Install dependencies for graphical user interface (X11+Openbox): 
```
pacman -S xorg-server
pacman -S xf86-video-omapfb
pacman -S openbox
pacman -S xorg-xinit
pacman -S xf86-video-fbdev
pacman -S xf86-video-vesa
```
To start openbox:
`xinit /usr/bin/openbox`

- Add a regular system user
- Configure autologon 
- Configure autostart of Graphical User Interface: 
- Add to ~/.profile  `echo BB-I2C1 > /sys/devices/bone_capemgr.6/slots`
- Dependencies to run a pure X11 GUI (without Openbox).
`pacman -S xterm`
(config at `/etc/X11/xinit/xinitrc`; X11 by default tries to autostart xterm)
`startx`

References
-------------------------

http://beagleboard.org/Support/BoneScript 
http://code.enthought.com/chaco 
http://datko.net/2013/11/03/bbb_i2c 
http://elinux.org/Beagleboard:BeagleBoneBlack 
http://learn.adafruit.com/downloads/pdf/setting-up-io-python-library-on-beaglebone-black.pdf 
http://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/i2c 
http://letsmakerobots.com/files/userpics/u19048/B_3PinOut3.png 
http://makingaquadrotor.wordpress.com/2012/07/08/i2c-on-the-beaglebone 
http://minix-i2c.blogspot.com.br/2013/07/using-i2c-tools-with-angstrom-linux-on.html 
http://pyqwt.sourceforge.net 
http://stackoverflow.com/questions/17951155/implementing-pyqtgraph-for-live-data-graphing 
http://wiki.analog.com/resources/tools-software/linux-drivers/input-misc/adxl345 
http://wiki.openwrt.org/doc/techref/opkg 
http://www.adminempire.com/beaglebone-basics-for-arch-linux 
http://www.alfonsomartone.itb.it/mzscbb.html 
http://www.armhf.com/index.php/boards/beaglebone-black/#saucy 
http://www.elecrow.com/cooperated-designers-c-127/embedded-lab-c-127_128/easy-pulse-v11-p-837.html 
http://www.elinux.org/Beagleboard:BeagleBone_Black_FAQ 
http://www.elinux.org/Beagleboard:BoneScript 
http://www.i2cdevlib.com/devices/adxl345#source 
http://www.instructables.com/id/BeagleBone-Ubuntu-OS-LXDE-GUI/?ALLSTEPS 
http://www.michaelhleonard.com/understanding-and-using-i2c 
http://www.qcustomplot.com 
http://www.shantanubhadoria.com/article/setting-up-device-smbus-on-beaglebone-black-76 
http://www.swharden.com/blog/2013-05-08-realtime-data-plotting-in-python 
https://github.com/adafruit/adafruit-beaglebone-io-python 
https://github.com/adafruit/PyBBIO 
https://github.com/derekmolloy/beaglebone 
https://github.com/kelly/node-i2c 
https://github.com/mariobaldini/beagle-sensors 
https://github.com/rossant/galry 
https://github.com/timbit123/ADXL345 
https://github.com/zlalanne/node-serial-gui 
https://groups.google.com/forum/#!topic/beagleboard/YctTkwyFc8g 
https://lkml.org/lkml/2009/7/1/436 
https://www.youtube.com/watch?v=8C2zk6B-eLU 


#### Authors: 
- Mario Baldini 	<mario.baldini@ieee.org>
- Joao Baggio 		<jbaggio@gmail.com>
- Raimes Moraes 	<raimes@eel.ufsc.br>
