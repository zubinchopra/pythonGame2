SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "Linear Equation Solver"
PROBLEM_VERSION = "1.1"
PROBLEM_AUTHORS = ['Anoop Narra, Zubin Chopra']
PROBLEM_CREATION_DATE = "20-APR-2017"

PROBLEM_DESC=\
 '''The following problem will help the user in solving a simple linear
    equation. The solutions will use the SOLUZION format and works with
    the given demo equation."
'''


lhs = ["+", "3", "+", "7", "-", "2", "*", "x"]
OPERATORS = []
value = []
x = float(lhs[1])
sum = 0
INITIAL_STATE = lhs

def operatorFunc():
    global OPERATORS
    array_length = len(lhs)
    OPERATORS = []
    value[:] = []
    for num in range (0, array_length - 1):
        if(num % 2 == 0):
            if(lhs[num + 1] != "x"):
                if(lhs[num] == "+" and (num + 2 <= array_length - 1) and (lhs[num + 2] == "*" or lhs[num + 2] == "/")):
                    if(num + 2 <= array_length - 1):
                        if(lhs[num + 2] == "*"):
                            OPERATORS.append("Divide " + lhs[num + 1] + " from both sides")
                            value.append(lhs[num + 1])
                        elif(lhs[num + 2] == "/"):
                            OPERATORS.append("Multiply " + lhs[num + 1] + " from both sides")
                            value.append(lhs[num + 1])
                elif(lhs[num] == "-" and (num + 2 <= array_length - 1) and (lhs[num + 2] == "*" or lhs[num + 2] == "/" and lhs[num + 1] != 'x')):
                    if(num + 2 <= array_length - 1):
                        if(lhs[num + 2] == "*"):
                            OPERATORS.append("Divide both sides by -" + lhs[num + 1])
                            value.append(lhs[num + 1])
                        elif(lhs[num + 2] == "/"):
                            OPERATORS.append("Multiply by both sides by -" + lhs[num + 1])
                            value.append(lhs[num + 1])
                elif(lhs[num] == "-" and lhs[num + 2] != 'x'):
                    OPERATORS.append("Add " + lhs[num + 1] + " to both sides")
                    value.append(lhs[num + 1])
                elif(lhs[num] == "+" and lhs[num + 2] != 'x'):
                    OPERATORS.append("Subtract " + lhs[num + 1] + " from both sides")
                    value.append(lhs[num + 1])
                elif(lhs[num] == "*" and lhs[num + 2] != 'x'):
                    OPERATORS.append("Divide " + lhs[num + 1] + " from both sides")
                    value.append(lhs[num + 1])
                elif(lhs[num + 2] != 'x'):
                    OPERATORS.append("Multiply " + lhs[num + 1] + " from both sides")
                    value.append(lhs[num + 1])

def evaluate(index):
    global sum;
    option = OPERATORS[index][:1]
    del OPERATORS[index]
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
                number = float(lhs[num])
                value.pop(index)
                if(sign == '/' and lhs[num - 1] == '-'):
                    for i in range (0, len(lhs) - 1):
                        if(lhs[i] == '+'):
                            lhs[i] == '-'
                        elif(lhs[i] == '-'):
                            lhs[i] == '+'
                        elif(i % 2 == 1 and lhs[i] != 'x'):
                            lhs[i] = str(float(lhs[i] / number))
                    lhs[num - 1] = '+'
                    sum = sum * number * -1
                elif(sign == '*' and lhs[num - 1] == '-'):
                    for i in range (0, len(lhs) - 1):
                        if(lhs[i] == '+'):
                            lhs[i] = '-'
                        elif(lhs[i] == '-'):
                            lhs[i] = '+'
                        elif(lhs[i] != 'x'):
                            val = float(lhs[i])
                            lhs[i] = str(val / number)
                    sum = -1 * sum / number
                elif(sign == '/'):
                    sum = sum * number
                else:
                    sum = sum / number;
        elif(lhs[num] == option and lhs[num + 1] == value[index]):
            sign = lhs.pop(num)
            number = float(lhs.pop(num))
            if(sign == '+'):
                value.pop(index);
                sum = sum - number;
            else:
                value.pop(index)
                sum = sum + number;



def copy_state(s):
    return lhs

def goal_test(s):
  return (lhs[0] == "x" or (lhs[0] == "+" and lhs[1] == "1.0" and lhs[2] == "x"))

def get_sum():
    global sum
    return sum

def get_operators():
    global OPERATORS
    return OPERATORS


BRIFL_SVG = True
def use_BRIFL_SVG():
  global render_state
  #from  Missionaries_SVG_VIS_FOR_BRIFL import render_state as rs
  #render_state = rs
  from  Missionaries_SVG_VIS_FOR_BRIFL import render_state

operatorFunc()
evaluate(2)

operatorFunc()
evaluate(1)

operatorFunc()
evaluate(0)

print(sum)
print(OPERATORS)
print(value)
