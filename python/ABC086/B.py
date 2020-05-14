number = list(input().split())
int_number = int("".join(number))
for i in range(1,1000):
  if i ** 2 == int_number:
    print("Yes")
    exit()
print("No")
