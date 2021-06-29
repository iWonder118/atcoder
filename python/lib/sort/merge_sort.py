def merge(numbers, left, mid, right):
    L = numbers[left:mid]
    R = numbers[mid:right]
    for i in range(left, right):
        if len(L) == 0:
            numbers[i] = R.pop(0)
        elif len(R) == 0:
            numbers[i] = L.pop(0)
        elif L[0] <= R[0]:
            numbers[i] = L.pop(0)
        else:
            numbers[i] = R.pop(0)


def merge_sort(numbers, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(numbers, left, mid)
        merge_sort(numbers, mid, right)
        merge(numbers, left, mid, right)
        print(numbers)


# n = int(input())
# numbers = list(map(int, input().split()))
numbers = [8, 5, 3, 12, 14, 2]
n = len(numbers)
merge_sort(numbers, 0, n)
print(numbers)
