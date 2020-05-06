import math

x = int(input())
saving = 100
count = 0
while not x <= saving:
  saving = math.floor(saving + saving * 0.01)
  count += 1
print(count)