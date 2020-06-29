n = int(input())
a = [int(input()) for _ in range(n)]
a_sort = sorted(a, reverse=True)
for i in range(n):
    if a[i] == a_sort[0]:
        print(a_sort[1])
    else:
        print(a_sort[0])
