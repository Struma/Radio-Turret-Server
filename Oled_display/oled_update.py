#!/bin/env python
#This is a short python script that updates information to the oled display for the Pi Server

from lib_oled96 import ssd1306
import subprocess
from smbus import SMBus
import time


ip_ad = subprocess.check_output("ifconfig wlan0 | egrep 'inet\ ' | awk '{print $2}'", shell=True )[:-1]

total_disk = subprocess.check_output("df -h | grep /dev/root | awk '{print $2}'", shell=True)[:-1]

used_disk = subprocess.check_output("df -h | grep /dev/root | awk '{print $4}'", shell=True)[:-1]

mem = subprocess.check_output("top -n 1 -b | grep avail | awk '{print $9}'", shell=True)[:-1]

load_avrg = subprocess.check_output("top -n 1 -b | grep 'load aver' | awk '{print $(NF-2), $(NF-1), $(NF)}'", shell=True)[:-1]

i2cbus = SMBus(1)        

oled = ssd1306(i2cbus)   

#border around the screen:
oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

oled.canvas.text((7,3),    'SSH Pi @', fill=1)
oled.canvas.text((65,3), ip_ad, fill=1)
oled.canvas.text((7,15), "Load avgs:", fill=1)
oled.canvas.text((26,27), load_avrg, fill=1)
oled.canvas.text((7,39), "Ram use: " + mem + " K", fill=1)
oled.canvas.text((7,50), "Free dsk: " + used_disk + "/" + total_disk, fill=1)

oled.display()








