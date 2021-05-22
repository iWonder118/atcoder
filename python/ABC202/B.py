s = list(input())
s.reverse()
ans = ""
for word in s:
    if word == "6":
        ans += "9"
    elif word == "9":
        ans += "6"
    else:
        ans += word
print(ans)
