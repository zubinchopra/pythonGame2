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
<<<<<<< HEAD:p2.py
    value[:] = []
=======
>>>>>>> bf5eb1670df7f19d080668b6887bcb73ae0d4d44:p2/p2.py
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
<<<<<<< HEAD:p2.py
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
=======
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
>>>>>>> bf5eb1670df7f19d080668b6887bcb73ae0d4d44:p2/p2.py
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
                number = float(lhs[num])
                print(value.pop(index))
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
        print(lhs)
<<<<<<< HEAD:p2.py
        print("sum = ", sum)


=======
        print(sum)
    operatorFunc()
>>>>>>> bf5eb1670df7f19d080668b6887bcb73ae0d4d44:p2/p2.py

def copy_state(s):
    return lhs

def goal_test(s):
<<<<<<< HEAD:p2.py
  return (lhs[0] == "x" or (lhs[0] == "+" and lhs[1] == "1.0" and lhs[2] == "x"))
=======
  return (lhs[0]=="x" or (lhs[0]=="+" and lhs[1]=="x"))
>>>>>>> bf5eb1670df7f19d080668b6887bcb73ae0d4d44:p2/p2.py

def get_sum():
    global sum
    return sum
<<<<<<< HEAD:p2.py

def get_operators():
    global OPERATORS
    return OPERATORS


=======

def get_operators():
    global OPERATORS
    return OPERATORS


>>>>>>> bf5eb1670df7f19d080668b6887bcb73ae0d4d44:p2/p2.py
BRIFL_SVG = True
def use_BRIFL_SVG():
  global render_state
  #from  Missionaries_SVG_VIS_FOR_BRIFL import render_state as rs
  #render_state = rs
  from  Missionaries_SVG_VIS_FOR_BRIFL import render_state

operatorFunc()
<<<<<<< HEAD:p2.py
evaluate(0)

operatorFunc()
evaluate(1)

operatorFunc()
evaluate(0)
=======
>>>>>>> bf5eb1670df7f19d080668b6887bcb73ae0d4d44:p2/p2.py
print(OPERATORS)
print(value)
