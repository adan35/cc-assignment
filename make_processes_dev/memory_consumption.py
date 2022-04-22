import os
from os.path import exists
from memory_profiler import memory_usage

def memory_consumption(shared_num):
  path = './files/memory-consumption.txt'
  if exists(path):
    os.remove(path)
  while shared_num.value == 1:
    open(path, 'a').write(str(round(memory_usage(-1, 60, 60)[0])) + ',')