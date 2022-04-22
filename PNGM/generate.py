from make_processes_dev.is_prime import is_prime

def prime_numbers(start, end, shared_num):
  lst = []

  with open('./files/prime-numbers.txt', 'w') as f:
    if start < 2:
      start = 2
      lst.append(start)
      num = str(start) + ','
      f.write(num)

    if start % 2 == 0:
      start += 1

    for i in range(start, end+1, 2):
      if is_prime(i):
        lst.append(i)
        num = str(i) + ','
        f.write(num)

  shared_num.value = 0
  return lst
