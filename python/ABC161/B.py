n, m= map(int, (input().split()))
a = list(map(int, input().split()))
count = 0
total = 0
for i in a:
  total += i
for j in a:
  if not (j // total < 1 // (4 * m)):
    count += 1
if count >= m:
  print("Yes")
else:
  print("No")