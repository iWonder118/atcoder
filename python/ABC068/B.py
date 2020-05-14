def main():
	N = int(input())
	binary_list = [1,2,4,8,16,32,64]
	diff_n2binary = []
	for binary in binary_list:
		if binary <= N:
			diff_n2binary.append(abs(N - binary))
	print(binary_list[ diff_n2binary.index( min( diff_n2binary ) ) ] )

if __name__ == "__main__":
	main()