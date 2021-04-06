t = int(input())
cases = [int(input()) for _ in range(t)]

for case in cases:
    if case % 4 == 0:
        print("Even")
    elif case % 4 != 0 and case % 2 == 0:
        print("Same")
    else:
        print("Odd")