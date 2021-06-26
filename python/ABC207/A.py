cards = list(map(int, input().split()))
cards.sort(reverse=True)
print(sum(cards[:2]))
