import copy


def merge_sort(numbers, left, right):
    if right - left == 1:
        return numbers
    mid = left + (right - left) // 2
    merge_sort(numbers, left, mid)
    merge_sort(numbers, mid, right)

    copy_numbers = copy.deepcopy(numbers[left:mid])
    copy_numbers.extend(copy.deepcopy(numbers[mid:right + 1:-1]))
    index_left = 0
    index_right = len(copy_numbers)
    for i in range(left, right):
        if copy_numbers[index_left] <= copy_numbers[index_right]:
            index_left += 1
            numbers[i] = copy_numbers[index_left]
        else:
            index_right -= 1
            numbers[i] = copy_numbers[index_right]


# n = int(input())
# numbers = list(map(int, input().split()))
numbers = [8, 5, 3, 12, 14]
n = len(numbers)
merge_sort(numbers, 0, n)
print(numbers)
