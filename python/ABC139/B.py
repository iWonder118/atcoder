a, b = map(int, input().split())
consent = 1
tap_count = 0
while(consent < b):
  consent += a - 1
  tap_count += 1
print(tap_count)