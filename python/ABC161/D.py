k = int(input())
runrun_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in range(12,100001):
  num_list = list(str(i))
  count = 0
  for j in range(len(num_list) - 1):
    if abs(int(num_list[j]) - int(num_list[j + 1])) == 1:
      count += 1
  if (count - 1) == len(num_list):
    runrun_num.append(i)
print(runrun_num[k - 1])