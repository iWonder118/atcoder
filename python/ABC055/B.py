n = int(input())
training = 1
for i in range(1, n + 1):
    training = i * training % (10 ** 9 + 7)
print(training)
