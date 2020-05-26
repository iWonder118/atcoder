n = int(input())
a = list(map(int, input().split()))

student_turn = [0] * (n + 1)
for i in range(n):
  student_turn[a[i] - 1] = i + 1
student_turn.pop()
print(" ".join(map(str,student_turn)))