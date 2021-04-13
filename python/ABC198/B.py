n = input()
flg = False
for i in range(10):
    copy_n = list("0" * i + n)
    reversed_copy_n = reversed(copy_n)
    if "".join(copy_n) == "".join(reversed_copy_n):
        print("Yes")
        exit()

print("No")
