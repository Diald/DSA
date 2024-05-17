class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        #to start an empty tree
        self.root = None
    def insert(self,value):
        new_node = Node(value)
        temp = self.root
        if(self.root is None):
            self.root = new_node
            return True
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    def containsTree(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

new_tree = BinaryTree()
new_tree.insert(42)
new_tree.insert(72)
new_tree.insert(21)
print(new_tree.root.value)
print(new_tree.root.left.value)
print(new_tree.root.right.value)
print(new_tree.containsTree(1))
            
        
