n = int(input())
places = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
can_move = True
for i in range(1, n + 1):
  _t = places[i][0] - places[i - 1][0]
  _x = abs(places[i][1] - places[i - 1][1])
  _y = abs(places[i][2] - places[i - 1][2])

  if not _t >= _x + _y or not _t % 2 == (_x + _y) % 2:
    can_move = False
    break

if can_move:
  print("Yes")
else:
  print("No")
