q, h, s, d = map(int, input().split())
n = int(input())
cheep_1 = min(q * 4, 2 * h, s)
if 2 * cheep_1 <= d:
    print(cheep_1 * n)
else:
    n1 = n % 2
    print(n // 2 * d + n1 * cheep_1)
