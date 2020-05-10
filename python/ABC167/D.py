n, k = map(int, input().split())
towns = list(map(int, input().split()))
place_count = [0] * (n + 1)
next_place = 1
teleport_count = 0
for i in range(n * 2):
  place_count[next_place] += 1
  next_place = towns[next_place - 1]
one_move_place = place_count.count(1)
for place in place_count:
  if place > 1:
    teleport_count += 1
next_place = 1
for _ in range(one_move_place + (k - one_move_place) % teleport_count):
  next_place = towns[next_place - 1]
print(next_place)