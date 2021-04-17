n, m = map(int, input().split())
numbers_a = set(map(int, input().split()))
numbers_b = set(map(int, input().split()))
ans = []

for number in numbers_a:
    if not (number in numbers_b):
        ans.append(number)

for number in numbers_b:
    if not (number in numbers_a):
        ans.append(number)
if len(ans) != 0:
    ans.sort()
    print(" ".join(map(str, ans)))
else:
    print("")
