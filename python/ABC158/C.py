import math

def per8_and_per10(n, a, b):
  per8  = n * 0.08 
  per10 = n * 0.1
  if a <= f01_rounding(per8) < a+1 and b <= f01_rounding(per10) < b+1:
    return True
  else:
    return False

def f01_rounding(number):
  number_str = list(str(number))
  number_str_slice = "".join(number_str[:(number_str.index("."))])
  number_int = int(number_str_slice)
  return number_int

a, b = map(int, input().split())
for i in range(1,1010):

  if per8_and_per10(i, a, b):
    print(i)
    exit()
print(-1)