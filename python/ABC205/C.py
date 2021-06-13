a, b, c = map(int, input().split())
is_odd = c % 2 == 1
if is_odd:
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")

else:
    if abs(a) > abs(b):
        print(">")
    elif abs(a) < abs(b):
        print("<")
    else:
        print("=")
