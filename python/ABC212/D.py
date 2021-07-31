import heapq


q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
pri_queue = []
heapq.heapify(pri_queue)
plus = 0
for i in range(q):
    if query[i][0] == 1:
        heapq.heappush(pri_queue, query[i][1])
    elif query[i][0] == 2:
        plus += query[i][1]
    else:
        print(heapq.heappop(pri_queue) + plus)
