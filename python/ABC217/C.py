n = int(input())
numbers = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    ans[numbers[i] - 1] = i + 1
print(" ".join(map(str, ans)))
