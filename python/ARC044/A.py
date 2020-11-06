# import math


# def get_sieve_of_eratosthenes(n):
#     if not isinstance(n, int):
#         raise TypeError('n is int type.')
#     if n < 2:
#         raise ValueError('n is more than 2')
#     prime = []
#     limit = math.sqrt(n)
#     data = [i + 1 for i in range(1, n)]
#     while True:
#         p = data[0]
#         if limit <= p:
#             return prime + data
#         prime.append(p)
#         data = [e for e in data if e % p != 0]


# n = int(input())
# if n == 1:
#     print("Not Prime")
#     exit()
# primes = get_sieve_of_eratosthenes(n)
# str_n = str(n)
# digit_total = sum(map(int, list(str_n)))
# if n in primes:
#     print("Prime")
#     exit()
# if int(str_n[-1]) % 2 != 0 and int(str_n[-1]) != 5 and digit_total % 3 != 0:
#     print("Prime")
#     exit()
# print("Not Prime")
n = int(input())
primes = [2, 3, 5]
if n == 1:
    print("Not Prime")
else:
    if n in primes:
        print("Prime")
        exit()
    for i in range(3):
        if n % primes[i] == 0:
            print("Not Prime")
            exit()
    print("Prime")
