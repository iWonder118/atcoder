n = int(input())
numbers = list(map(int, input().split()))
ans = []
for i in range(1, n):
    temp1 = 0
    temp2 = 0
    for number in numbers[:i]:
        temp1 |= number
    for number in numbers[i:]:
        temp2 |= number
    ans.append(temp1 ^ temp2)
print(min(ans))
