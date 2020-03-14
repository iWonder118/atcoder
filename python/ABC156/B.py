def Base_10_to_n(X, K):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%K)+out
        X_dumy = int(X_dumy/K)
    return out
n, k = map(int, input().split())
print(len(Base_10_to_n(n, k)))