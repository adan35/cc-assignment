from multiprocessing import Process, Value
from PNGM.generate import prime_numbers
from make_processes_dev.cpu_consumption import cpu_consumption
from make_processes_dev.memory_consumption import memory_consumption
from make_processes_dev.time_duration import time_duration

def make_processes(start, end):
  shared_num = Value('i', 1)
  p1 = Process(target=(prime_numbers), args=(start, end, shared_num,))
  p2 = Process(target=(cpu_consumption), args=(shared_num,))
  p3 = Process(target=(memory_consumption), args=(shared_num,))
  p4 = Process(target=(time_duration), args=(shared_num,))
  p1.start()
  p2.start()
  p3.start()
  p4.start()
  p1.join()
  p2.join()
  p3.join()
  p4.join()
