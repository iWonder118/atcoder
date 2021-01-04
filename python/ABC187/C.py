import collections


n = int(input())
words = [input() for _ in range(n)]
words_Count = collections.Counter(words)
dict_words_Count = dict(words_Count)
for word, num in dict_words_Count.items():
    if "!" in word:
        word = word.replace("!", "")
        word_num = words_Count[word]
        if word_num != 0:
            print(word)
            exit()
print("satisfiable")
