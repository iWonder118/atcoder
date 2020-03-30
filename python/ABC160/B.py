x  = int(input())
happy = 0
if x // 500 > 0:
  happy += 1000 * (x // 500)
x %= 500
if x // 5 > 0:
  happy += 5 * (x // 5)
print(happy)