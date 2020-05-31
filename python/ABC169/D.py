import math

def sieve_of_eratosthenes(target):
  dest = int(math.sqrt(target))
  target_list = list(range(2, target + 1))
  prime_list = []

  while True:
    num_min = min(target_list)
    if num_min >= dest:
      prime_list.extend(target_list)
      break
    prime_list.append(num_min)

    i = 0

    while True:
      if i >= len(target_list):
        break
      elif target_list[i] % num_min == 0:
        target_list.pop(i)
      i += 1

  print(prime_list)

n = int(input())

sieve_of_eratosthenes(n)