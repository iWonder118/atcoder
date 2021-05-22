import collections


n = int(input())
sequence_a = list(map(int, input().split()))
sequence_b = list(map(int, input().split()))
sequence_c = list(map(int, input().split()))
ans = 0

sequence_d = list(map(lambda x: sequence_b[x - 1], sequence_c))
count_sequence_d = dict(collections.Counter(sequence_d))
isExist = False
for k in sequence_a:
    if k in count_sequence_d:
        ans += count_sequence_d[k]

print(ans)
