import copy


l, q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(q)]
trees = [[1, l]]
for i in range(q):
    if query[i][0] == 1:
        tmp = []
        for tree in trees:
            if tree[0] <= query[i][1] and query[i][1] < tree[1]:
                tmp.append([tree[0], query[i][1]])
                tmp.append([query[i][1] + 1, tree[1]])
            else:
                tmp.append(tree)
        trees = copy.deepcopy(tmp)
    else:
        for tree in trees:
            if tree[0] <= query[i][1] and query[i][1] < tree[1]:
                print(tree[1] - tree[0] + 1)
