s = input()
n = int(input())
todo = [list(map(int, input().split())) for _ in range(n)]
for st, en in todo:
    s_copy = s
    reverse_str = s_copy[st - 1:en]
    s = s_copy[:st - 1] + reverse_str[::-1] + s_copy[en:]
print(s)
