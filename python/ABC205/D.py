n, q = map(int, input().split())
numbers = list(map(int, input().split()))
query = [int(input()) for _ in range(q)]
max_num = max(numbers)
min_num = min(numbers)
between = max_num - n
for i in range(q):
    num = query[i]
    if between < num:
        print(max_num + num - between)
    elif num < min_num:
        print(num)
    else:
        for j in range(1, n):
            if numbers[j - 1] <= num and num <= numbers[j]:
                print(num + j)
                break
