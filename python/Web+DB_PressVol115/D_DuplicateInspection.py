n = int(input())
a = [int(input()) for i in range(n)]
how_many = [0] * (n+1)
how_many[0] = -1
for i in a:
  how_many[i] +=1
if how_many.count(1) == n:
  print("Correct")
else:
  print("{} {}".format(how_many.index(2), how_many.index(0)))