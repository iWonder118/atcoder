N = int(input())
r = str(input())
total = 0
for i in range(N):
    if r[i] == "A":
        total += 4
    elif r[i] == "B":
        total += 3
    elif r[i] == "C":
        total += 2
    elif r[i] == "D":
        total += 1
print(total / N)
