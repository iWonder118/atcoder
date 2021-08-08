h, w, n = map(int, input().split())
number_cards = [list(map(int, input().split())) for _ in range(n)]
cards = [[0] * w for _ in range(h)]
for i in range(n):
    cards[number_cards[i][0]][number_cards[i][1]] = i + 1
    