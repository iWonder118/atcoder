n = int(input())
words = [list(input()) for _ in range(n)]
dict_words = dict()
ans = 0
for i in range(n):
    words[i].sort()
    sort_word = "".join(words[i])
    if sort_word in dict_words.keys():
        dict_words[sort_word] += 1
    else:
        dict_words[sort_word] = 1
for v in dict_words.values():
    if v != 1:
        ans += v * (v - 1) // 2
print(ans)
