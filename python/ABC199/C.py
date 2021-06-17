n = int(input())
s = list(input())
pre = s[:n]
post = s[n:]
q = int(input())
for i in range(q):
    t, a, b = input().split()
    a, b = int(a), int(b)
    if t == '1':
        if b <= n:
            pre[a - 1], pre[b - 1] = pre[b - 1], pre[a - 1]
        elif n < a:
            post[a - n - 1], post[b - n - 1] = post[b - n - 1], post[a - n - 1]
        else:
            pre[a - 1], post[b - n - 1] = post[b - n - 1], pre[a - 1]
    else:
        pre, post = post, pre

print(''.join(pre + post))
