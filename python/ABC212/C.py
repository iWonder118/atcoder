def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while 1 < right - left:
        mid = (left + right) // 2
        if value == data[mid]:
            return 0
        elif abs(value - data[mid - 1]) >= abs(value - data[mid]):
            left = mid
        else:
            right = mid
    return min(abs(data[left] - value), abs(data[right] - value))


n, m = map(int, input().split())
numbers_a = sorted(list(map(int, input().split())))
numbers_b = sorted(list(map(int, input().split())))
ans = 10 ** 9 + 1
for i in range(n):
    ans = min(ans, binary_search(numbers_b, numbers_a[i]))
print(ans)
