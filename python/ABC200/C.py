from collections import Counter


n = int(input())
numbers = list(map(int, input().split()))
count = 0
numbers_mod200 = list(map(lambda x: x % 200, numbers))
mod200_Count = dict(Counter(numbers_mod200))
for i in range(n):
    if mod200_Count[numbers_mod200[i]] > 1:
        count += mod200_Count[numbers_mod200[i]] - 1
    mod200_Count[numbers_mod200[i]] = mod200_Count[numbers_mod200[i]] - 1

print(count)