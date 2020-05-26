n = int(input())
foods = list(map(int, input().split()))
foods.sort()
for i in range(1,n):
  foods[i] = (foods[i - 1] + foods[i]) / 2
print(foods[n-1])