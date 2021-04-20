import collections


s = list(input())
count_dict_value = list(dict(collections.Counter(s)).values())
if len(count_dict_value) != 3:
    [count_dict_value.append(0) for _ in range(3 - len(count_dict_value))]
for i in range(len(count_dict_value)):
    for j in range(len(count_dict_value)):
        if i != j:
            if abs(count_dict_value[i] - count_dict_value[j]) > 1:
                print("NO")
                exit()
print("YES")
