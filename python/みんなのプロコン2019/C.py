k, a, b = map(int, input().split())
k -= 1
if a >= b:
    print(k + 2)
else:
    time = k // a
    mod = k % a
    if k >= time * 2:
        print(b * time + mod)
    else:
        print(b * (time - 1) + mod + a)
