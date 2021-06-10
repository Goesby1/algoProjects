# Given a list of strings containing integers and arithmetic operators ordered
# by reverse polish notation, evaluate the expression.
# Valid operators are +, -, *, / .
# We will use truncated integer division here. For example, 13/6 = 2.
# Also, whenever we have [operand1 operand2 operator], operand 1 always comes first.
# So, [“7” “2”,  “-”] is  7 - 2, and [“13”, “6”, “/”] is 13/6.
# For this question, you will get only +, *, -, and /, and have no invalid inputs.
# All lists will be in appropriate RPN order. If an empty list is provided, return 0.
# Return all outputs as integers (not strings)

# How it works
# In reverse polish notation, operators are put after the operands. So for example,
# instead of writing 3 + 4, we write 3 4 +. The steps to evaluating an RPN expression
# are as follows.

# 1. Evaluate operators left to right. Starting with the leftmost operator,
# 2. Given the operator you’re currently on, apply it to the two operands directly
#    before it. Remove the operator and its operands , and replace them with the result.
# 3. Repeat step one with the next operator on the left hand side, if there is one.
#    Otherwise, the final result is your answer.

from typing import List

#Check if the character is and integer
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def evalRPN(tokens: List[str]) -> int:
    #copy list
    cpyList = tokens.copy()
    indexC = -1
    #check that the list is valid
    if (len(tokens) == None or len(tokens) == 0) :
        return 0
    for index, value in enumerate(tokens): 
        
        #Keeps track of the cpylist index we do the operations on
        indexC += 1 
        
        if isInt(value) == False:
            #If the character is an int then get the 2 operands before it
            fin = 0
            op1 = int(cpyList[indexC - 2])
            op2 = int(cpyList[indexC - 1])
            #Calculate the operation
            if (value == '-') :
                fin = op1 - op2

            elif (value == '+'):
                fin = op1 + op2

            elif (value == '/'):
                fin = op1/op2

            elif (value == '*'):
                fin = op1 * op2
            #Pop the operation and operands that were just performed 
            cpyList.pop(indexC)
            cpyList.pop(indexC - 1)
            #Place the calculated value into cpyList
            cpyList[indexC - 2] = str(int(fin))
            #Reset the indexC value 
            indexC = indexC - 2
    return int(cpyList[0])

    #I create a copy of the list and use indexC value todo operation on the proper values. cpylist keeps getting smaller
    #until there is only one value left. 
    #The space complexity is O(n) where n is the size of the original list tokens
    #The time complexity is O(n) since we have to check every value in the list


        


