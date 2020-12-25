n = int(input())
flowers = list(map(int, input().split()))
if flowers.count(0) == 0:
    ans = 1
else:
    ans = 1 + flowers.count(0)
while True:
    flowers = list(map(lambda x: max(-1, x - 1), flowers))
    flowers = list(map(lambda x: -1 if x == 0 else x, flowers))
    tmp = "".join(map(str, flowers)).split("-1")
    if flowers.count(-1) == n:
        break
    ans += len(tmp) - tmp.count("")
print(ans)
