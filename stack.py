class Stack:
    def __init__(self):
        self.items=[]
        
    # push method for adding the elements to the stack
    def push(self,items):
        self.items.append(items)
    
    # pop method for removing the top element from the stack  
    def pop(self):
       return self.items.pop()
        
    # to check wheather the stack is empty or not
    def isEmpty(self):
        return self.items == []
    
    # it returns the last element of the stack
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    # to reverse the elements of the stack
    def rev(self):
            return self.items.reverse()  #or can use list slicing return self.items[::-1]
    # to print the stack
    def showStack(self):
        return self.items
    

# stack= Stack()
# # stack.isEmpty()
# print(stack.isEmpty())
# stack.push("Mohit")
# stack.push("Bisht")
# stack.push("123")
# stack.push("mohit2")
# # print(stack.isEmpty())
# print(stack.peek())
# stack.rev()
# print(stack.showStack())