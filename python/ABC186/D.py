N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
ans = 0
for i in range(1, N):
    ans += i * A[i]
for j in range(N - 1):
    ans -= (N - 1 - j) * (A[j])
print(ans)
