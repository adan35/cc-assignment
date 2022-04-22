
from os.path import exists

def all_records():
  file1 = './files/time.txt'
  file2 = './files/cpu-consumption.txt'
  file3 = './files/memory-consumption.txt'
  if not exists(file1):
    f = open(file1, 'a')
    f.close()
  if not exists(file2):
    f = open(file2, 'a')
    f.close()
  if not exists(file3):
    f = open(file3, 'a')
    f.close()
  with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'r') as f3:
    lst = []
    dict = {}
    content1 = f1.read()
    content1 = content1.split(',')
    content1.pop()
    
    content2 = f2.read()
    content2 = content2.split(',')
    content2.pop()
    
    content3 = f3.read()
    content3 = content3.split(',')
    content3.pop()
    
    for i in range(len(content1)):
      lst.append({
        "time_stamp": str(content1[i]),
        "cpu": str(content2[i]),
        "memory": str(content3[i])
      })
    
    dict["prime_nums"] = lst
    
    return dict


def k_records(k):
  records_dict = all_records()
  records_list = records_dict["prime_nums"]
  if k > len(records_list):
    k = len(records_list)
  print(len(records_list))
  
  k_record = []
  for i in range(len(records_list)-1, len(records_list)-k-1, -1):
    k_record.append(records_list[i])
  
  return k_record

