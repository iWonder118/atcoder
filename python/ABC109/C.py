import math


n, x = map(int, input().split())
cities = list(map(int, input().split()))

if abs(x - cities[0]) == 0:
    ans = abs(x - cities[1])
else:
    ans = abs(x - cities[0])

for i in range(n):
    ans = math.gcd(ans, abs(x - cities[i]))
print(ans)
# distances = []
# cities.sort()
# for i in range(n - 1):
#     if cities[i] <= x <= cities[i + 1]:
#         distances.append(x - cities[i])
#         distances.append(cities[i + 1] - x)
#     else:
#         distances.append(cities[i + 1] - cities[i])
# if distances != []:
#     print(min(distances))
# else:
#     print(cities[0] - x)
