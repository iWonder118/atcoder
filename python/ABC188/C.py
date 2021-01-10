import copy


n = int(input())
players = list(map(int, input().split()))
copy_arr = copy.deepcopy(players)
while n > 1:
    tmp = []
    for a, b in zip(copy_arr[::2], copy_arr[1::2]):
        tmp.append(max(a, b))
    copy_arr = tmp
    n -= 1
print(players.index(min(copy_arr)) + 1)
