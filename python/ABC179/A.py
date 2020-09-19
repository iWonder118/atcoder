s = list(input())
len_s = len(s)
if s[len_s - 1] == "s":
    print("".join(s) + "es")
else:
    print("".join(s) + "s")
