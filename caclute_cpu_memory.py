#!/usr/bin/env python
from psutil import *
import time

interval_seconds = 1
num = 0.
cpu = 0.
cpu_mean = 0.
mem_mean = 0.
mem = 0.
f = open('./cpu_mem.txt','w+')
f.write("\t"+"time"+"\t"*2 + "cpu_used"+"\t"+ "cpu_used_mean"+"\t"+"memoty_used"+"\t"+"memoty_used_mean"+"\n")
while True:
  num+=1
  cpupercent = float('%.1f' % cpu_percent(interval=interval_seconds))
  cpu += cpupercent
  cpu_mean = float('%.1f' % (cpu/num))
  virtualmemory = float('%.1f' % virtual_memory()[2])
  mem += virtualmemory
  mem_mean = float('%.1f' % (mem/num))
  f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\t ")
  f.write(str(cpupercent)+"\t "*2)
  f.write(str(cpu_mean)+"\t "*2)
  f.write(str(virtualmemory)+"\t"*2)
  f.write(str(mem_mean)+"\n")
f.close()
	
