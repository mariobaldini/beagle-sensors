
BeagleBone Black Misc Experiments with Health Sensors
==============




Overview 
---------------


#### Hardware: #### 
- Beaglebone Black
- ADXL 345 (accelerometer)
- . (air flow sensor) TODO: air flow part number


#### Software: ####  
- Archlinux
- ic2tools (general i2c tools)
- Python (for raw sensor access)
- X11 / Openbox (for graphical display)


#### Data Input/Output Options: #### 
- Serial connect (Header pin or USB serial)
- Standard HDMI video + mouse + keyboard
- SSH (text mode and graphical, through -X option)


#### Future improvements ####
- Dynamic DNS for easier network access
- Clean openbox right click menu
- Customize openbox right click to call functions of the system
- Linux Device Drivers for abstracted access of the hardware?
- Improve syncronization techniques of data sampling (hardware interrupt?)
- MOSH support
- GUI access over network
- Cape design, with generic connectors. (P2 ?)
- Filesystem improvements (to avoid dirty state on sequencial hard power offs)




Installation guide
-------------------------



(requirements: a linux machine to create the SDcard using this guide. Beaglebone documentation also describe how to create using Windows)

### Easy mode: ###
Install a pre-built disk image to a SDcard: 
`sudo dd if=arch-build.img of=/dev/SDCardNAME`
`sudo fdisk -l `

TODO: docs




*Protip:* (-- not that pro, :P)
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
TODO Documentation

- Configure autologon: 
TODO Documentation

- Configure autostart of Graphical User Interface: 
TODO Documentation


- (Optional) Dependencies to run a pure X11 GUI (without Openbox).
`pacman -S xterm`
(config at `/etc/X11/xinit/xinitrc`; X11 by default tries to autostart xterm)
`startx`






Software usage 
-------------------------


TODO: docs

Reading devices on a I2C bus:






#### temporary scratchpad; fully experimental!! ####
** just for reference to where the vanilla code is / how to run it**
TODO: propper organize it.

``


code v1
src/v1/main.py


run:
python2 main.py


``







#### Authors: ####
- Mario Baldini 	<mario.baldini@ieee.org>
- Joao Baggio 		<jbaggio@gmail.com>
- Raimes Moraes 	<raimes@eel.ufsc.br>





/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE":
 * <mario.baldini@ieee.org> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return. -- Mario Baldini
 * ----------------------------------------------------------------------------
 */