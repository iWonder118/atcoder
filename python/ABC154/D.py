n, k = map(int, input().split())
dices = list(map(int, input().split()))
expected = []
tmp = 0
for dice in dices:
    tmp += (1 + dice) / 2
    expected.append(tmp)
# for i in range(n - k + 1):
#     ans.append(sum(expected[i:i + k]))
ans = [expected[k - 1]]
for i in range(k, n):
    ans.append(expected[i] - expected[i - k])
print(max(ans))
