def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n = int(input())
ans = 0
for i in range(1, n):
    n_c = n - i
    divisors = make_divisors(n_c)
    
    for j in range(len(divisors)):
        if n_c % divisors[j] == 0:
            ans += 1
print(ans)
