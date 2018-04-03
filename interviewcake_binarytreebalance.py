"""Write a function to see if a binary tree "superbalanced" (a new tree property we just made up).

A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.

Here's a sample binary tree node class:"""

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
new_tree.insert_left(0)
new_tree.insert_right(4)

# MY IMPLEMENTATION
# def get_height(new_tree, left_counter=0, right_counter=0):
#     if not new_tree.left and not new_tree.right: #if both left & right nodes have no more children
#         return max(left_counter,right_counter)
#     if new_tree.left: # if left node has children
#         left_counter += 1
#         print "LEFT COUNTER IS " + str(left_counter)
#         return get_height(new_tree.left, left_counter, right_counter) # don't need return?
#     if new_tree.right: # if right node has children
#         right_counter += 1
#         print "RIGHT COUNTER IS " + str(left_counter)
#         return get_height(new_tree.right, left_counter, right_counter)

# RUBY'S IMPLEMENTATION
def get_height(node):
    if not node:
        return 0
    else:
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        return max(left_height, right_height) + 1

print get_height(new_tree)

def is_balanced(node):
    # want to see if height of left & right side of trees are =
    if not node:
        return True
    height_left = get_height(node.left)
    height_right = get_height(node.right)
    if height_left == height_right and is_balanced(node.left) and is_balanced(node.right):
        return True
    return False
print is_balanced(new_tree)

