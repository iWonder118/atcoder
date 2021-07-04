import copy


n, k = map(int, input().split())
numbers = list(map(int, input().split()))
copy_numbers = copy.deepcopy(numbers)
copy_numbers.sort()
dict_numbers = dict()
index = 0
for num in copy_numbers:
    dict_numbers[num] = index
    index += 1
product = k // n
mod = k % n
for num in numbers:
    ans = product
    if mod >= dict_numbers[num] + 1:
        ans += 1
    print(ans)
