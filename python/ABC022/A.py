n, s, t = map(int, input().split())
w = int(input())
A = [int(input()) for _ in range(n - 1)]
A.insert(0,0)
best_body = 0

for i in range(len(A)):
  w += A[i]

  if w >= s and w <= t:
    best_body += 1

print(best_body)