n = int(input())
towns = [list(map(int, input().split())) for _ in range(n)]
a_vote = 0
for i in range(n):
    a_vote += towns[i][0]

for i in range(n):
    
