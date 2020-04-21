from stack import Stack

def isMatch(parenthesis1,parenthesis2):
    if parenthesis1 == "{" and parenthesis2 == "}":
        return True
    elif parenthesis1 == "(" and parenthesis2 == ")":
        return True
    elif parenthesis1 == "[" and parenthesis2 == "]":
        return True
    else: 
        return False

def isBalance(parenthesis):
    stack1 = Stack()
    isBalance = True
    index = 0
    
    while index < len(parenthesis) and isBalance:
        if parenthesis[index] in "({[":
            stack1.push(parenthesis[index])
        
        else:
            if stack1.isEmpty():
                isBalance = False
            else:
                top = stack1.pop()
                if not isMatch(top,parenthesis[index]):
                    isBalance = False
        
        index +=1
        
    if stack1.isEmpty() and isBalance:
        return True
    else:
         return False
     
    
print(isBalance("))"))