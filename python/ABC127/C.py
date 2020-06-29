n, m = map(int, input().split())
Authority = [list(map(int, input().split())) for _ in range(m)]
cards = list(range(1, n + 2))
l_list = []
r_list = []
for i in range(m):
    l_list.append(Authority[i][0])
    r_list.append(Authority[i][1])
        
print(len(cards[max(l_list):min(r_list) + 1]))
