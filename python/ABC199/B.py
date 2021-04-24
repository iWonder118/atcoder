n = int(input())
numbers_a = list(map(int, input().split()))
numbers_b = list(map(int, input().split()))
ans = min(numbers_b) - max(numbers_a) + 1
if ans < 0:
    print(0)
else:
    print(ans)