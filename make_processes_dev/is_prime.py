def is_prime(num):
  if num < 2:
    return False
  j = 2
  while(j * j <= num):
    if(num % j == 0):
      return False
    j += 1
  return True
