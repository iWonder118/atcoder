n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for _ in range(m):
    A.append(10 ** 9 + 1)
for _ in range(n):
    B.append(10 ** 9 + 1)
A.sort(reverse=True)
B.sort(reverse=True)
total = 0
count = 0
for i in range(n + m):
    time = min(A[-1], B[-1])
    if A[-1] == time:
        total += A.pop()
    elif B[-1] == time:
        total += B.pop()
    if total > k:
        break
    count += 1
print(count)
