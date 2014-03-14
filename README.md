
BeagleBone Black Tools for Physiological Data Acquisition
============================




Overview 
---------------

_TODO: picture_



#### Hardware:  
- Beaglebone Black
- ADXL 345 (accelerometer)
- . (air flow sensor) _TODO: air flow part number_


#### Software:   
- Archlinux
- ic2tools (general i2c tools)
- Python (for raw sensor access)
- X11 / Openbox (for graphical display)


#### Data Input/Output Options:  
- Serial connect (Header pin or USB serial)
- Standard HDMI video + mouse + keyboard
- SSH (text mode and graphical, through -X option)


**Sample output:**
```
0.0,0.0,0.0    0.0,0.0,0.0    0.0,0.0,0.0    0.0,0.0,0.0    0.0    0.0    0.0    0.0
```
4x ADXL345 accelerometers and 4x Analog pins. 




##### Benefits from using a Beaglebone+Linux instead a Microcontroller based approach:

_TODO: docs_





#### Future improvements 
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


Installation guide
-------------------------



(requirements: a linux machine to create the SDcard using this guide. Beaglebone documentation also describe how to create using Windows)

### Easy mode: 
Install a pre-built disk image to a SDcard: 
`sudo dd if=arch-build.img of=/dev/SDCardNAME`
`sudo fdisk -l `

Pre-built images:  
[https://drive.google.com/folderview?id=0B8FdkQxARKjHbFNFeVJmNUdJazQ&usp=sharing]

_TODO: docs_




*Protip:* (-- not that Pro)
Connect your Beagle to the network, find out its IP address (`ifconfig`) and control it over SSH and write code through a network mounted volume. It's way easier to control it over your home machine and you can even run the GUI over SSH (`-X`) without a full setup. 
The whole setup results in a Beagle+USB cable (for power and serial over USB); and not a keyboard, monitor, hdmi cables, etc. 


### Advanced install (from scratch): ###


- Install Archlinux to a sdcard: 
http://archlinuxarm.org/platforms/armv7/ti/beaglebone-black

- Default user/passwd: root/root

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


- Add a regular system user (run as root is a bad practice)
_TODO Documentation_

- Configure autologon: 
_TODO Documentation_

- Configure autostart of Graphical User Interface: 
_TODO Documentation_


- (Optional) Dependencies to run a pure X11 GUI (without Openbox).
`pacman -S xterm`
(config at `/etc/X11/xinit/xinitrc`; X11 by default tries to autostart xterm)
`startx`






Software usage 
-------------------------


_TODO: docs_

Reading devices on a I2C bus:






#### temporary scratchpad; fully experimental!! ####
**just for reference to where the vanilla code is / how to run it**  
_TODO: propper organize it_

```
code v1
src/v1/main.py


run:
python2 main.py





ubuntu

sudo su  (# -> root)

apt-get update
apt-get install i2c-tools screen htop nmon

echo BB-I2C1 > /sys/devices/bone_capemgr.9/slots
ls -l /sys/bus/i2c/devices/i2c-*


i2cdetect -l   (busca portas )
i2cdetect -y -r 1   (busca devices na porta)

i2cdump -y 2 0x53
i2cget -y 2 0x53 00


ADAFruit Python libs

sudo ntpdate pool.ntp.org
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip -y
sudo easy_install -U distribute  //debian only
sudo pip install Adafruit_BBIO


sudo apt-get install python-smbus



test code:
import Adafruit_BBIO.ADC as ADC
ADC.setup()

# le valor na faixa 0-1.0
p40_norm = ADC.read("P9_40")
p40_raw = ADC.read_raw("P9_40")
print 'ADC P9_40\t Normalizado: ', p40_norm, '\tADC P9_40 RAW: ', p40_raw

# esperado:
# ADC P9_40     Normalizado:  0.796111106873     ADC P9_40 RAW:  1464.0








Gráficos: (em andamento / incompleto)


pacman -S xorg-server xorg-server-utils xorg-xinit


```







#### Authors: 
- Mario Baldini 	<mario.baldini@ieee.org>
- Joao Baggio 		<jbaggio@gmail.com>
- Raimes Moraes 	<raimes@eel.ufsc.br>




```
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE": 
 * [http://en.wikipedia.org/wiki/Beerware]
 * <mario.baldini@ieee.org> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return. -- Mario Baldini
 * ----------------------------------------------------------------------------
 */
 ```