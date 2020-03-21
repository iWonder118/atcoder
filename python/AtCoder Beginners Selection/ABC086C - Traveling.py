n = int(input())
places = [list(map(int, input().split())) for _ in range(n)]
now_place = [0] * 2
ans = 0
before_t = 0
for place in places:
  move_x = abs(place[1] - now_place[0]) 
  move_y = abs(place[2] - now_place[1])
  if (place[0] - before_t) < (move_x + move_y) or (place[0] - before_t) % 2 != (move_x + move_y) % 2:
    ans += 1
  now_place[0] = place[1]
  now_place[1] = place[2]
  before_t = place[0]
if ans == 0:
  print("Yes")
else:
  print("No")