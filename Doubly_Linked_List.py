class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self,value):
        n = Node(value)
        self.head = n
        self.tail = n
        self.length = 1
    def printDLL(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next
    def append(self,value):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.length +=1
        return True
    def popDLL(self):
        if self.head is None:
            return False
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return True
    def prependDLL(self,value):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
        self.length+=1
        return True
    def popFirst(self):
        if self.length==0:
            return False
        temp = self.head
        if self.length==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp
    def getDLL(self,index):
        if index<0 or index>self.length:
            return False
        if index<self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length-1,index,-1):
                temp = temp.prev
        return temp
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return temp
        return False
    def insertDLL(self,index,value):
        n = Node(value)
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prependDLL(value)
        if index==self.length:
            return self.append(value)
        else:
            before = self.getDLL(index-1)
            after = before.next
            n.prev = before
            n.next = after
            before.next = n
            after.prev = n
    def removeDLL(self, index):
        if index < 0 or index >= self.length:
            return False
        if self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp = self.getDLL(index)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

        self.length -= 1
        return True
my_dll = DoublyLinkedList(7)
my_dll.append(10)
my_dll.append(20)
my_dll.append(30)
my_dll.removeDLL(3)
my_dll.printDLL()
