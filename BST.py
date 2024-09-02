class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def BFS(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)
        while(len(queue)>0):
            current_node = queue.pop()
            result.append(current_node.value)
            if(current_node.left is not None):
                queue.append(current_node.left)
            if(current_node.right is not None):
                queue.append(current_node.right)
        return result
    def DFS_preOrder(self):
        # eg- [47,21,76,18,27,52,82]
        result = []
        def traverse(current_node):
            result.append(current_node)
            if(current_node.left is not None):
                traverse(current_node.left)
            if(current_node.right is not None):
                traverse(current_node.right)
        traverse(self.root)
    def DFS_postOrder(self):
        # eg - [18,27,21,52,82,76,47]
        result = []
        def traversal(current_node):
            if(current_node.left is not None):
                traversal(current_node.left)
            if(current_node.right is not None):
                traversal(current_node.right)
            result.append(current_node.value)
        traversal(self.root)
        return result
