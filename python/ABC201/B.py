n = int(input())
mountains = [list(input().split()) for _ in range(n)]
sorted_mountains = sorted(mountains, key=lambda x: int(x[1]), reverse=True)
print(sorted_mountains[1][0])