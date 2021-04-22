n, p = map(int, input().split())
bisckets = list(map(int, input().split()))
contain_odd = False
for biscket in bisckets:
    if biscket % 2 == 1:
        contain_odd = True
if not contain_odd and p == 0:
    print(2 ** n)
elif not contain_odd and p == 1:
    print(0)
else:
    print(2 ** (n - 1))
