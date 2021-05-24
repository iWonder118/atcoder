n, c, k = map(int, input().split())
times = [int(input()) for _ in range(n)]
times.sort()
passenger = 0
ans = 1
departure = times[0] + k
for time in times:
    if passenger == c or departure < time:
        ans += 1
        departure = time + k
        passenger = 1
    else:
        passenger += 1

print(ans)
