def make_divisors(n):
  lower_divisors , upper_divisors = [], []
  i = 1
  while i*i <= n:
    if n % i == 0:
      lower_divisors.append(i)
      if i != n // i:
        upper_divisors.append(n//i)
    i += 1
  return lower_divisors + upper_divisors[::-1]

n = int(input())
a = list(map(int, input().split()))
list_divisors = []
ans = 0
for i in range(n):
  list_divisor = make_divisors(a[i])
  
  if list_divisors & a.remove(a[i]) == 0:
    ans += 1
print(ans)