n, m = map(int, input().split())
scores = [input() for _ in range(n)]
odd_count = 0
even_count = 0
for i in range(n):
    if scores[i].count("1") % 2 == 1:
        odd_count += 1
    else:
        even_count += 1
print(odd_count * even_count)