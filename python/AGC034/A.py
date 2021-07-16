n, a, b, c, d = map(int, input().split())
s = input()
 
if '##' in s[a-1:max(c,d)]:
    print('No')
else:
    if c < d:
        print('Yes')
    else:
        if s[b-2] == '.' and  s[b] == '.':
            print('Yes')
        elif s[d-2] =='.' and s[d] == '.':
            print('Yes')
        elif '...' in s[b-1:d]:
            print('Yes')
        else:
            print('No')