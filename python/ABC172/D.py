def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return len(lower_divisors + upper_divisors[::-1])


def sigma(frm, to):
    result = 0
    memo = [0] * (to + 1)
    for i in range(frm, to + 1):
        divisors = make_divisors(i)
        result += i * divisors
        memo[i] = divisors
    print(result)


n = int(input())

sigma(1, n)
