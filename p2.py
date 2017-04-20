lhs = ["+", "3", "+", "7", "-", "2", "*", "x"]
operators =[]
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
                            print("Divide " + lhs[num + 1] + " from both sides")
                        elif(lhs[num + 2] == "/"):
                            print("Multiply " + lhs[num + 1] + " from both sides")
                elif(lhs[num] == "-" and (num + 2 <= array_length - 1) and (lhs[num + 2] == "*" or lhs[num + 2] == "/")):
                    if(num + 2 <= array_length - 1):
                        if(lhs[num + 2] == "*"):
                            print("Divide " + lhs[num + 1] + " from both sides")
                        elif(lhs[num + 2] == "/"):
                            print("Multiply " + lhs[num + 1] + " from both sides")
                elif(lhs[num] == "-"):
                    print("Add " + lhs[num + 1] + " from both sides")
                elif(lhs[num] == "+"):
                    print("Subtract " + lhs[num + 1] + " from both sides")
                elif(lhs[num] == "*"):
                    print("Divide " + lhs[num + 1] + " from both sides")
                else:
                    print("Multiply " + lhs[num + 1] + " from both sides")

operatorFunc()
