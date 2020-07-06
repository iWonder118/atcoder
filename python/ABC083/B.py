n, a, b = map(int, input().split())
total = 0
for i in range(1, n + 1):
    num = 0
    str_i = str(i)
    list_i = list(str_i)
    for j in range(len(list_i)):
        num += int(list_i[j])
    if a <= num and num <= b:
        total += i
print(total)
