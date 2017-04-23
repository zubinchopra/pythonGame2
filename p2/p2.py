SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "Linear Equation Solver"
PROBLEM_VERSION = "1.1"
PROBLEM_AUTHORS = ['Anoop Narra, Zubin']
PROBLEM_CREATION_DATE = "20-APR-2017"

PROBLEM_DESC=\
 '''The <b>"Missionaries and Cannibals"</b> problem is a traditional puzzle
in which the player starts off with three missionaries and three cannibals
on the left bank of a river.  The object is to execute a sequence of legal
moves that transfers them all to the right bank of the river.  In this
version, there is a boat that can carry at most three people, and one of
them must be a missionary to steer the boat.  It is forbidden to ever
have one or two missionaries outnumbered by cannibals, either on the
left bank, right bank, or in the boat.  In the formulation presented
here, the computer will not let you make a move to such a forbidden situation, and it
will only show you moves that could be executed "safely."
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
                elif(lhs[num] == "-" and (num + 2 <= array_length - 1) and (lhs[num + 2] == "*" or lhs[num + 2] == "/")):
                    if(num + 2 <= array_length - 1):
                        if(lhs[num + 2] == "*"):
                            OPERATORS.append("Divide both sides by -" + lhs[num + 1])
                            value.append(lhs[num + 1])
                        elif(lhs[num + 2] == "/"):
                            OPERATORS.append("Multiply by both sides by -" + lhs[num + 1])
                            value.append(lhs[num + 1])
                elif(lhs[num] == "-"):
                    OPERATORS.append("Add " + lhs[num + 1] + " to both sides")
                    value.append(lhs[num + 1])
                elif(lhs[num] == "+"):
                    OPERATORS.append("Subtract " + lhs[num + 1] + " from both sides")
                    value.append(lhs[num + 1])
                elif(lhs[num] == "*"):
                    OPERATORS.append("Divide " + lhs[num + 1] + " from both sides")
                    value.append(lhs[num + 1])
                else:
                    OPERATORS.append("Multiply " + lhs[num + 1] + " from both sides")
                    value.append(lhs[num + 1])

def evaluate(index):
    global sum;
    option = OPERATORS[index][:1]
    del OPERATORS[index]
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
        print(value)
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

def copy_state(s):
    return lhs

def goal_test(s):
  return (lhs[0]=="x" or (lhs[0]=="+" and lhs[1]=="x"))

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
print(OPERATORS)
print(value)
