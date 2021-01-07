from collections import Counter


n = int(input())
problems = list(map(int, input().split()))
m = int(input())
productions = list(map(int, input().split()))
problems_count = Counter(problems)
productions_count = Counter(productions)
for production in set(productions):
    if 0 > problems_count[production] - productions_count[production]:
        print("NO")
        exit()
    else:
        pass
print("YES")
