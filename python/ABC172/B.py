s = list(input())
t = list(input())
count = 0
for i, j in zip(s, t):
    if i != j:
        count += 1
print(count)
