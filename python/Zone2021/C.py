n = int(input())
members = [list(map(int, input().split())) for _ in range(n)]
member1 = 0
member1_index = 0
for i in range(n):
    if member1 < sum(members[i]):
        member1 = sum(members[i])
        member1_index = i
for i in range(n):
    for j in range(n):
        if i != j != member1_index:
            max(member[i]