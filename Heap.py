class Heap:
    def __init__(self):
        self.heap = [] #define the heap using adjacency list
    def parent_index(self,index):
        # to find the index of parent
        return (index-1)//2
    def left_child_index(self,index):
        # to find the index of left child
        return 2*(index)+1
    def right_child_index(self,index):
        return 2*(index)+2
    def parent_value(self,index):
        return self.heap[self.parent_index]
    def left_child_value(self,index):
        return self.heap[self.left_child_index]
    def right_child_value(self,index):
        return self.heap[self.right_child_index]
    def swap(self,index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    def insert(self,value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index>0 and self.parent_value(index) < value:
            self.swap(index, self.parent_index(index))
            index = self.parent_index(index)
        return
    def remove(self):
        if(len(self.heap)==0):
            return None
        if(len(self.heap)==1):
            return self.heap.pop()
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        heapify_down(0)
        return value
    def heapify_down(self,index):
        max_index = index
        while True:
            left_index = self.left_child_index(index)
            right_index = self.right_child_index(index)
            if(left_index<len(self.heap) and self.heap[left_index]>self.heap[max_index]):
                self.swap(left_index,max_index)
                max_index = left_index
            if(right_index<len(self.heap) and self.heap[right_index]>self.heap[max_index]):
                self.swap(right_index,max_index)
                max_index = right_index
            if(max_index!=index):
                self.swap(max_index,index)
                index = max_index
            else:
                return 
        return
    
