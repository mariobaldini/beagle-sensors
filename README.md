beagle-sensors
==============

BeagleBone Black Misc Experiments with Health Sensors



## Overview ##

Hardware:
- Beaglebone Black
- ADXL 345 (accelerometer)
- ? (air flow sensor)
- 


Software: 
- Archlinux
- ic2tools (general i2c tools)
- Python (for raw sensor access)
- X11 / Openbox (for graphical display)


Data Input/Output Options: 
- Serial connect (Header pin or USB serial)
- Standard HDMI video + mouse + keyboard
- SSH (text mode and graphical, through -X option)

Protip: 
Connect your Beagle to the network 




## Installation guide ##
(requirements: a linux machine to create the SDcard using this guide. Beaglebone documentation also describe how to create using Windows)

Easy mode: 
Install a pre-built disk image to a SDcard: 

sudo dd if=arch-build.img of=/dev/SDCardNAME

sudo fdisk -l 
TODO Documentation



Advanced install (from scratch):


Install Archlinux to a sdcard: 
http://archlinuxarm.org/platforms/armv7/ti/beaglebone-black

Default user/passwd: root/root

Update de system: 
pacman -Syu 


Install dependencies for graphical user interface (X11+Openbox): 
pacman -S xorg-server
pacman -S xf86-video-omapfb
pacman -S openbox
pacman -S xorg-xinit
pacman -S xf86-video-fbdev
pacman -S xf86-video-vesa

To start openbox:
xinit /usr/bin/openbox



Add a regular system user (run as root is a bad practice)
TODO Documentation

Configure autologon: 
TODO Documentation

Configure autostart of Graphical User Interface: 
TODO Documentation


(Optional) Dependencies to run a pure X11 GUI (without Openbox).
pacman -S xterm
(config at /etc/X11/xinit/xinitrc; X11 by default tries to autostart xterm)
startx






## Software usage ##


Reading devices on a I2C bus:















