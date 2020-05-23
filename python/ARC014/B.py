n = int(input())
words = [input() for _ in range(n)]
duel = "DROW"
player1 = []
player2 = []

for i in range(n):
  if words[i] == words[i] and i % 2 == 0:
    duel = "LOSE"
  elif words[i][-1::] != words[i][:-1 * (len(words[i]) - 1) :] and i % 2 == 0:
    duel = "LOSE"
  elif words[i] == words[i] and i % 2 == 1:
    duel = "WIN"
  elif words[i][-1::] != words[i][:-1 * (len(words[i]) - 1) :] and i % 2 == 1:
    duel = "WIN"

  player1.append(words[i]) if i % 2 == 0 else player2.append(words[i])
  
  if player1.count(words[i]) > 1:
    duel ="LOSE"
  elif player2.count(words[i]) > 1:
    duel ="WIN"

print(duel)