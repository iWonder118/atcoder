n = int(input())
numbers = list(map(int, input().split()))
num_memo = [0] * 200001
flag = True
for number in numbers:
    num_memo[number] = 1
    if number != 0 and flag is True:
        print(0)
    else:
        flag = False
        print(num_memo.index(0))
