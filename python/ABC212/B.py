password = list(map(int, list(input())))
count = 0
for i in range(3):
    if password[i] == 9:
        if password[i + 1] == 0:
            count += 1
    else:
        if password[i] + 1 == password[i + 1]:
            count += 1
if len(set(password)) == 1 or count == 3:
    print("Weak")
else:
    print("Strong")
