import string

word = list(input())
odd_count = 0
even_count = 0
for i in range(len(word)):
    if (i + 1) % 2 == 1 and word[i] in string.ascii_lowercase:
        odd_count += 1
    elif (i + 1) % 2 == 0 and word[i] in string.ascii_uppercase:
        even_count += 1
if odd_count + even_count == len(word):
    print("Yes")
else:
    print("No")
