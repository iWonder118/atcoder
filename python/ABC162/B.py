n = int(input())
total = 0
for i in range(1,n+1):
  if not (i % 5 == 0 or i % 3 == 0):
    total += i
print(total)