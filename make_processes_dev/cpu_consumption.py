import os
import psutil
from os.path import exists

def cpu_consumption(shared_num):
  path = './files/cpu-consumption.txt'
  if exists(path):
    os.remove(path)
  while shared_num.value == 1:
    open(path, 'a').write(str(round(psutil.cpu_percent(60))) + ',')