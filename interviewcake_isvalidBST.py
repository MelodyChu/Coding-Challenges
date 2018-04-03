# Check that binary tree is valid binary search tree

# how is insert left & insert right correct here?
class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

new_tree = BinaryTreeNode(3)
new_tree.insert_left(2)
new_tree.insert_left(1)
new_tree.insert_left(100)
new_tree.insert_right(4)

#CHECK THIS IMPLEMENTATION
def is_valid(node): #breadth first; want to check each
    if not node:
        return True
    if not node.left and not node.right:
        return True # need to confirm this definition
    if node.left.value < node.value and node.right.value > node.value:
        print "Node left value is " + str(node.left.value)
        print "Node right value is " + str(node.right.value)
        is_valid(node.left)
        print "left"
        is_valid(node.right)
        print "right"
    # else:
    #     return False
    return is_valid(node.left) and is_valid(node.right)

print is_valid(new_tree)

# FROM http://www.koderdojo.com/blog/verify-binary-search-tree-is-valid-in-python
def is_valid_2(root):
    if root is None:
        return True 
    def check_bst(node,min1,max1):
        if node.value < min1:
            return False
        if node.value > max1:
            return False
        left_check = True
        right_check = True
        if node.left is not None: # <= node.value
            left_check = check_bst(node.left, min1, node.value)
        if node.right is not None:
            right_check = check_bst(node.right, node.value, max1)

        return left_check and right_check

    return check_bst(root, float('-inf'), float('inf'))








