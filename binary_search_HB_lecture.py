class Node(object):
    
    def __init__(self, data, children):
        self.data = data
        if not children:
            self.children = []
        else:
            self.children = children
            
    def find(self, sought):
        
        to_visit = [self]

        while to_visit:
            current = to_visit.pop()
            
            if current.data == sought:
                return current
            else:
                # didn't find in current, so going to children
                to_visit.extend(current.children)
                
    # recursively
                
    # def find(self, sought):
    #     to_visit = [self]
        
    #     while to_visit:
    #         current = to_visit.pop()
            
    #         if current.data == sought:
    #             return current
    #         else:
    #             find(current, sought)
    
class binaryNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def findbinaryNode(self, sought):
        current = self #recursively, can I just use self here too? instead of current?
        
        if current.data == sought:
            return current #returns the node
        

        elif current.data < sought:
            return findbinaryNode(current.left, sought)
            
        elif current.data > sought:
            return findbinaryNode(current.right, sought)

class binaryTree(object):
    def __init__(self, root):
        self.root = root

root = binaryNode(3)
first_left = binaryNode(2)
first_right = binaryNode(4)
second_right = binaryNode(5)

binaryTree(root)
root.left = first_left
root.right = first_right
first_right.right = second_right

def getheight(node):
    if not node:
        return 0
    else:
        left_height = getheight(node.left)
        right_height = getheight(node.right)
        return max(left_height, right_height) + 1

print getheight(root)


def if_balanced(node):
    if not node:
        return True
    left_height = getheight(node.left)
    right_height = getheight(node.right)
    if abs(left_height - right_height) <= 1 and if_balanced(node.left) and if_balanced(node.right):
        return True
    return False

            
# Given a sorted (increasing order) array, write an algorithm to create a binary tree with
#minimal height.
# [1,2,3,4,5]
                
    
    
    