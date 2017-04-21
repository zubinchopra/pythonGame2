lhs = ["+", "3", "+", "7", "-", "2", "*", "x"]
operators = []
value = []
x = float(lhs[1])
sum = 0

def operatorFunc():
    array_length = len(lhs)
    for num in range (0, array_length - 1):
        if(num % 2 == 0):
            if(lhs[num + 1] != "x"):
                if(lhs[num] == "+" and (num + 2 <= array_length - 1) and (lhs[num + 2] == "*" or lhs[num + 2] == "/")):
                    if(num + 2 <= array_length - 1):
                        if(lhs[num + 2] == "*"):
                            operators.append("Divide " + lhs[num + 1] + " from both sides")
                            value.append(lhs[num + 1])
                        elif(lhs[num + 2] == "/"):
                            operators.append("Multiply " + lhs[num + 1] + " from both sides")
                            value.append(lhs[num + 1])
                elif(lhs[num] == "-" and (num + 2 <= array_length - 1) and (lhs[num + 2] == "*" or lhs[num + 2] == "/")):
                    if(num + 2 <= array_length - 1):
                        if(lhs[num + 2] == "*"):
                            operators.append("Divide both sides by -" + lhs[num + 1])
                            value.append(lhs[num + 1])
                        elif(lhs[num + 2] == "/"):
                            operators.append("Multiply by both sides by -" + lhs[num + 1])
                            value.append(lhs[num + 1])
                elif(lhs[num] == "-"):
                    operators.append("Add " + lhs[num + 1] + " to both sides")
                    value.append(lhs[num + 1])
                elif(lhs[num] == "+"):
                    operators.append("Subtract " + lhs[num + 1] + " from both sides")
                    value.append(lhs[num + 1])
                elif(lhs[num] == "*"):
                    operators.append("Divide " + lhs[num + 1] + " from both sides")
                    value.append(lhs[num + 1])
                else:
                    operators.append("Multiply " + lhs[num + 1] + " from both sides")
                    value.append(lhs[num + 1])

def evaluate(index):
    global sum;
    option = operators[index][:1]
    print(option)
    if(option == "S"):
        option = "+"
    elif(option == "A"):
        option = "-"
    elif(option == "M"):
        option = "/"
    else:
        option = "*"
    array_length = len(lhs)
    for num in range (0, array_length - 2):
        if(option == '*' or option == '/'):
            if(lhs[num] == value[index] and lhs[num + 1] == option):
                sign = lhs.pop(num + 1)
                number = float(lhs.pop(num))
                if(sign == '/' and lhs[num - 1] == '-'):
                    lhs[num - 1] = '+'
                    sum = sum * number * -1
                elif(sign == '*' and lhs[num - 1] == '-'):
                    lhs[num - 1] = '+'
                    sum = -1 * sum / number
                elif(sign == '/'):
                    sum = sum * number
                else:
                    sum = sum / number;
        elif(lhs[num] == option and lhs[num + 1] == value[index]):
            sign = lhs.pop(num)
            number = float(lhs.pop(num))
            if(sign == '+'):
                sum = sum - number;
            else:
                sum = sum + number;
        print(lhs)
        print(sum)


operatorFunc()
print(operators)
print(value)
evaluate(0)
evaluate(1)
evaluate(2)
