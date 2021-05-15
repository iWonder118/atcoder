s = list(input())
included = []
not_included = []
ans = []
for i in range(len(s)):
    if s[i] == "o":
        included.append(i)
    elif s[i] == "x":
        not_included.append(i)
patterns = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                patterns.append([i, j, k, l])
for pattern in patterns:
    count = 0
    isEnable = False
    for num in included:
        if num in pattern:
            count += 1
    if len(included) == count:
        count2 = 0
        for num2 in not_included:
            if num2 in pattern:
                count2 += 1
        if count2 == 0:
            isEnable = True

    if isEnable:
        ans.append(pattern)
print(len(ans))