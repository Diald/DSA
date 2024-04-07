class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 
class Stack:
    def __init__(self,value):
        n = Node(value)
        self.top = n
        self.length = 1
    def printStack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return True
    def popStack(self):
        temp = self.top
        if self.length==0:
            return None
        if self.length==1:
            self.top = None
        else:
            self.top = self.top.next
            temp.next = None
        self.length-=1
        return temp.value
    def pushStack(self,value):
        new = Node(value)
        if self.length==0:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.length +=1
        return True
myStack = Stack(10)
myStack.pushStack(20)
myStack.pushStack(30)
myStack.popStack()
myStack.printStack()
