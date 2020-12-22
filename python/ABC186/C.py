def mod(n):
    num = n // 8
    mod = n % 8
    tmp = []
    if num == 0:
        return "".join(reversed(tmp))
    else:
        tmp.append(str(mod))
        return mod(num)


def main():
    n = int(input())
    ans = n
    for i in range(1, n + 1):
        print(mod(i))
        if "7" in str(i) or "7" in mod(i):
            ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
