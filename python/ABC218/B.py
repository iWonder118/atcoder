string = ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = list(map(int, input().split()))
ans = ""
for num in numbers:
    ans += string[num - 1]
print(ans)
