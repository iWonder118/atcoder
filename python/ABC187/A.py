a, b = input().split()
sum_a = sum(list(map(int, list(a))))
sum_b = sum(list(map(int, list(b))))
if sum_a > sum_b:
    print(sum_a)
else:
    print(sum_b)
