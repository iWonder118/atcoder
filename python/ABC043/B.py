input_list = list(input())
output = ""
for i in range(len(input_list)):
    if input_list[i] == "0":
        output += "0"
    elif input_list[i] == "1":
        output += "1"
    else:
        if len(output) > 0:
            output = output[:len(output) - 1]
print(output)
