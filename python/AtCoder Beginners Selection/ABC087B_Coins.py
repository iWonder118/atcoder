a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0
for i in range(a+1):
  sum_a = 500 * i
  for j in range(b+1):
    sum_b = 100 * j
    for k in range(c+1):
      sum_c = 50 * k
      if x == (sum_a + sum_b + sum_c):
        count += 1
print(count)