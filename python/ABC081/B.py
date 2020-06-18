n = int(input())
a = list(map(int, input().split()))


count = 0

while True:
  even_count = 0
  for i in range(n):
    if a[i] % 2 == 0:
      even_count += 1

  if even_count == len(a):
    a = list(map(lambda x : x // 2, a))
    count += 1

  else:
    break

print(count)