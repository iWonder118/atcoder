from collections import Counter


n = int(input())
oranges = list(map(int, input().split()))
oranges_nums_keys = dict(Counter(oranges)).keys()
ans = []
for num in oranges_nums_keys:
    flag = False
    count = 0
    for j in range(n):
        if num <= oranges[j]:
            flag = True
            count += 1
        else:
            flag = False
    ans.append(num * count)
print(max(ans))
