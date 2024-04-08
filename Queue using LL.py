class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 
class Queue:
    def __init__(self,value):
        n = Node(value)
        self.first = n 
        self.last = n
        self.length = 1
    def printQueue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return True
    def enqueue(self,value):
        new = Node(value)
        if self.length==0:
            self.first = new
            self.last = new
        else:
            self.last.next = new
            self.last = new
        self.length+=1
        return True
    def dequeue(self):
        temp = self.first
        if self.length==0:
            return None
        if self.length==1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length-=1
        return True
myQueue = Queue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
myQueue.enqueue(40)
myQueue.dequeue()
myQueue.printQueue()
