def main():
	A, B, C = map(int, input().split())
	even_flag = True
	count = 0

	while even_flag:
		if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
			even_flag = False
			break

		elif A == B and B == C and A == C:
			break

		A, B, C = (B // 2 + C // 2), (A // 2 + C // 2), (A // 2 + B // 2)
		count += 1

	if even_flag:
		print(-1)
	else:
		print(count)
		
if __name__ == "__main__":
	main()