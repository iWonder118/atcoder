n = int(input())
employees = [list(map(int, input().split())) for _ in range(n)]
ans = 10 ** 9 + 1
for i in range(n):
    for j in range(n):
        ans = min(ans, employees[i][0] + employees[j][1] if i == j else max(employees[i][0], employees[j][1]))
print(ans)

