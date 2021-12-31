l, r = list(map(int, input().split()))
s = input()
ans = s[:l - 1]
ans += "".join(reversed(list(s[l - 1: r])))
ans += s[r:]
print(ans)
