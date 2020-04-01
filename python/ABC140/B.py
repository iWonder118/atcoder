n = int(input())
cuisine = list(map(int, input().split()))
saticefaction = list(map(int,input().split()))
moreSaticefaction = list(map(int, input().split()))
total = 0
beforeCuisine = -1
for i in cuisine:
  total += saticefaction[i - 1]
  if (i - 1) == beforeCuisine:
    total += moreSaticefaction[beforeCuisine - 1]
  beforeCuisine = i
print(total)