a, b, c = map(int, input().split())
if c == 0:
    if a - 1 < b:
        print("Aoki")
    else:
        print("Takahashi")
else:
    if b - 1 < a:
        print("Takahashi")
    else:
        print("Aoki")
