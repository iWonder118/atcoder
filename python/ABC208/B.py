import math


p = int(input())
count = 0
while p != 0:
    count += 1
    for i in sorted(list(range(1, 11)), reverse=True):
        if math.factorial(i) <= p:
            p -= math.factorial(i)
            break
print(count)
