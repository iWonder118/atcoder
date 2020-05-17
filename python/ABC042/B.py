n, l = map(int, input().split())
words = [input() for _ in range(n)]
words.sort()
print("".join(words))
