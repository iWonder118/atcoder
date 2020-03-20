cards = int(input())
numbers = list(map(int, input().split()))
Alice = 0
Bob = 0
numbers.sort(reverse = True)
count = 0
for number in numbers:
  if count % 2 == 0:
    Alice += number
  else:
    Bob += number
  count += 1
print(Alice - Bob)
