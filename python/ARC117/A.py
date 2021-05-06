a, b = map(int, input().split())
a_range_list = list(range(1, a))
b_range_list = list(range(1, b))
a_range_list.append(2000000)
b_range_list.append(sum(a_range_list) - sum(b_range_list))
print(" ".join([str(i) for i in a_range_list + [-j for j in b_range_list]]))

