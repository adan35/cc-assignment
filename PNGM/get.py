def get_prime_nums():
  lst = []
  with open("./files/prime-numbers.txt") as file:
    content = file.read()
    content = content.split(',')
    for i in content:
      lst.append(i)
  lst.pop()
  return lst