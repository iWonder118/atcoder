t = int(input())
test_case = [map(int,input().split()) for _ in range(t)]
goal = test_case[0] - test_case[4]
coin_cost = test_case.pop(0)
coin_cost.append(test_case[4])
coin_total = sum(coin_cost)

# dp[i] := i円を払う最小枚数
for m in range(1, coin_total):
  dp = [0] * coin_total
  dp[0] = 0
  for i in range(m+1):
    for e in coin_cost:
      if i-e >= 0:
        dp[i] = min(dp[i-e]+1, dp[i])
  dp[m]