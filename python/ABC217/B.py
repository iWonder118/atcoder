contenst_all = ["ABC", "ARC", "AGC", "AHC"]
contest = [input() for _ in range(3)]
print(list(set(contenst_all) - set(contest))[0])
