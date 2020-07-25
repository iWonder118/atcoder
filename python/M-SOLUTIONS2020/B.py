a, b, c = map(int, input().split())
k = int(input())
for i in range(k):
    if not a < b:
        b *= 2
    elif not b < c:
        c *= 2
    if a < b and b < c:
        print("Yes")
        exit()
print("No")
