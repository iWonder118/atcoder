import math

n = int(input())
X = math.ceil(n / 1.08)

if math.floor(X * 1.08) == n:
	print(X)
else:
	print(":(")