v, t, s, d = map(int, input().split())
time = d / v
if time < t and s < time:
    print("Yes")
else:
    print("No")