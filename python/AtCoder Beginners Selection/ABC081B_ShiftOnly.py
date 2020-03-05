n = int(input())
a = list(map(int, input().split()))
count = 0
while  n == len(list(filter(lambda x: x % 2 == 0, a))):
  for x in range(len(a)):
    a[x] /= 2
  count += 1
print(count)