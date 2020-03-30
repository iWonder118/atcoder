s = input()
week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
if s == "SUN":
  print(7)
else:
  print(week.index("SUN") - week.index(s))