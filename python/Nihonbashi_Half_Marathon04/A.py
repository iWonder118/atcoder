import random

n, m = map(int, input().split())
dice = [1, 2, 3, 4, 5, 6]
scores = [0] * (n+1)
for i in range(1, (m+1)):
  next_squre = {}
  next_squre_sroted = []
  
  a = random.randrange(0, 6, 1)
  if not scores.count(0) == 5:
    b = random.randrange(1, 7, 1)
  dice[a] = b
  print("{} {} {} {} {} {}".format(dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]))
  d, v, x = map(int, input().split())
  scores[x] = v
  move = 500 - x
  if move < 4:
    for j in range(x, (x + move + 1)):
      next_squre[j] = scores[j]
  else:
    for j in range(x, (x + 4)):
      next_squre[j] = scores[j]
  next_squre_sroted = sorted(next_squre.items(), key=lambda x:x[1], reverse=True)
  if scores.count(0) == 5:
    b = next_squre_sroted[0][0] - x