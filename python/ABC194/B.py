n = int(input())
empolyee = [list(map(int, input().split())) for _ in range(n)]
empolyee_dict = []
for i in range(n):
    empolyee_dict.append({"a": empolyee[i][0], "b": empolyee[i][1], "total": empolyee[i][0] + empolyee[i][1]})
empolyee_sorted_total = sorted(empolyee_dict, key=lambda x: x['total'])
empolyee_sorted_a = sorted(empolyee_dict, key=lambda x: x['a'])
empolyee_sorted_b = sorted(empolyee_dict, key=lambda x: x['b'])
print(empolyee_sorted_total)
print(empolyee_sorted_a)
print(empolyee_sorted_b)
pattrn1 = max(empolyee_sorted_a[0]["a"], empolyee_sorted_b[1]["b"])
pattrn2 = max(empolyee_sorted_a[1]["a"], empolyee_sorted_b[0]["b"])
print(min(min(pattrn1, pattrn2), empolyee_sorted_total[0]["total"]))
