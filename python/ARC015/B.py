from decimal import Decimal

N = int(input())

dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for _ in range(N):
	high, low = map(Decimal, input().split())
	if 35 <= high:
		dic[1] += 1
	if 30 <= high < 35:
		dic[2] += 1
	if 25 <= high < 30:
		dic[3] += 1
	if 25 <= low:
		dic[4] += 1
	if low < 0 and 0 <= high:
		dic[5] += 1
	if high < 0:
		dic[6] += 1

val = list(dic.values())
print(val[0], val[1], val[2], val[3], val[4], val[5])