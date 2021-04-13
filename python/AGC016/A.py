import string


s = input()
ans = 1000
for a in string.ascii_lowercase:
    if a in s:
        copy_s = s
        count = 0
        while len(copy_s) != copy_s.count(a):
            temp = ''
            for i in range(len(copy_s) - 1):
                if copy_s[i] == a or copy_s[i + 1] == a:
                    temp += a
                else:
                    temp += copy_s[i]
            count += 1
            copy_s = temp
        ans = min(count, ans)
print(ans)