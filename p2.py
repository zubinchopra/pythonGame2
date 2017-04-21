lhs = ["+", "3", "+", "7", "-", "2", "*", "x"]
operators = []
value = []
x = float(lhs[1])
sum = 0
array_length = len(lhs)

def operatorFunc():
    for num in range (0, array_length - 1):
        if(num % 2 == 0):
            if(lhs[num + 1] != "x"):
                if(lhs[num] == "+" and (num + 2 <= array_length - 1) and (lhs[num + 2] == "*" or lhs[num + 2] == "/")):
                    if(num + 2 <= array_length - 1):
                        if(lhs[num + 2] == "*"):
                            operators.append("Divide " + lhs[num + 1] + " from both sides")
                            value.append(float(lhs[num + 1]))
                        elif(lhs[num + 2] == "/"):
                            operators.append("Multiply " + lhs[num + 1] + " from both sides")
                            value.append(float(lhs[num + 1]))
                elif(lhs[num] == "-" and (num + 2 <= array_length - 1) and (lhs[num + 2] == "*" or lhs[num + 2] == "/")):
                    if(num + 2 <= array_length - 1):
                        if(lhs[num + 2] == "*"):
                            operators.append("Divide " + lhs[num + 1] + " from both sides")
                            value.append(float(lhs[num + 1]))
                        elif(lhs[num + 2] == "/"):
                            operators.append("Multiply " + lhs[num + 1] + " from both sides")
                            value.append(float(lhs[num + 1]))
                elif(lhs[num] == "-"):
                    operators.append("Add " + lhs[num + 1] + " from both sides")
                    value.append(float(lhs[num + 1]))
                elif(lhs[num] == "+"):
                    operators.append("Subtract " + lhs[num + 1] + " from both sides")
                    value.append(float(lhs[num + 1]))
                elif(lhs[num] == "*"):
                    operators.append("Divide " + lhs[num + 1] + " from both sides")
                    value.append(float(lhs[num + 1]))
                else:
                    operators.append("Multiply " + lhs[num + 1] + " from both sides")
                    value.append(float(lhs[num + 1]))

def evaluate(index):
    option = operators[index]][:1]
    if(option == "S"):
        option = "+"
    elif(option == "A"):
        option = "-"
    elif(option == "M"):
        option = "/"
    else:
        option = "*"
    for num in range (0, array_length - 1):
        if(option == "D" or option == "M"):
            if(lhs[num] == value[index] and lhs[num + 1] == option)


operatorFunc()
print(operators)
print(value)
