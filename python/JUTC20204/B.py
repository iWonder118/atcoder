n = int(input())
balls = [input().split() for i in range(n)]
red = []
blue = []
for ball in balls:
  if ball[1] == "R":
    red.append(int(ball[0]))
  else:
    blue.append(int(ball[0]))
red.sort()
blue.sort()
red.extend(blue)
print(" ".join(map(str,red)))