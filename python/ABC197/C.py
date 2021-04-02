n = int(input())
numbers = list(map(int, input().split()))
ans = 2 ** 30
for i in range(1 << (n - 1)):
    now = 0
    temp = 0
    for j in range(n):
        temp |= numbers[j]
        
        if i >> j & 1:
            now ^= temp
            temp - 0
    now ^= temp
    ans = min(ans, now)
    
print(ans)