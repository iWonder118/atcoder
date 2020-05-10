import collections

n = int(input())
words = [input() for _ in range(n)]
words_count = collections.Counter(words)
first_word = words[0]
word_end = first_word[0]
not_siritori = 0

for i in words_count.values():
  if i > 1:
    not_siritori += 1

for word in words:
  if word_end != word[0]:
    not_siritori += 1
  word_end = word[-1]

if not_siritori != 0:
  print("No")
else:
  print("Yes")