import os
import time
from os.path import exists

def time_duration(shared_num):
  path = './files/time.txt'
  if exists(path):
    os.remove(path)
  while shared_num.value == 1:
    time.sleep(60)
    result = time.localtime(time.time())
    s = str(result.tm_mday) + '-' + str(result.tm_mon) + '-' + str(result.tm_year) + ' ' + str(result.tm_hour) + ':' + str(result.tm_min) + ':' + str(result.tm_sec)
    open(path, 'a').write(s + ',')