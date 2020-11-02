n = int(input())
boad = [list(map(int, input().split())) for _ in range(n)]
ans = []
for low, high in boad:
    plus_low = low * (low - 1) // 2
    plus_high = high * (high + 1) // 2
    ans.append(plus_high - plus_low)
print(sum(ans))
