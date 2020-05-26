n = int(input())
diffcults = list(map(int, input().split()))
diffcults.sort()
ans = diffcults[n//2] - diffcults[n//2 - 1]
print(ans)