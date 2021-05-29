N = int(input())
A = list(map(int, input().split()))
x, z = 0, 0
y = sum(A)

for i in range(len(A) - 1):
    x = A[i]
    y -= x
    z += (x * y)

print(z % (10 ** 9 + 7))
