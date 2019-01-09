#!/usr/bin/env python2

import commands,time
	
ram = commands.getoutput('free -m |grep Mem').split()
print "My Ram is " + ram[1] + "MB\n"
cpu = commands.getoutput('lscpu | grep -i model | tail -1')     #taking cpu details from os
print cpu

print "@@@@@@@@@@@@@@@@@@@@@@@@@"
execfile('menu.py')
