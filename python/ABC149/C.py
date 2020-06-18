def is_prime(num):
  if num <= 1:
    return False
  
  i = 2
  while i ** 2 <= num:
    if num % i == 0:
      return False
    i += 1
    return True

x = int(input())

while not is_prime(x):
  x += 1
print(x)
