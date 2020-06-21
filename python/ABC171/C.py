import sys
import math

alphabet = [chr(i) for i in range(97, 97+26)]
result = []

def alphabet_decimal(v):
    quotient = math.floor(v / len(alphabet))
    surplus = v % len(alphabet)
    quotient -= 1 if surplus == 0 else 0
    surplus = len(alphabet) if surplus == 0 else surplus
    result.append(surplus)
    if len(alphabet) < quotient:
        alphabet_decimal(quotient)
    elif len(alphabet) < v:
        result.append(quotient)
    return "".join([alphabet[i - 1] for i in reversed(result)])

n = int(input())
print(alphabet_decimal(n))