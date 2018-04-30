# Problem: Implement BST class:
# first implement binary node class:
# then implement binary tree class, with add & contains methods

class BNode(object):
    """Binary Node class"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    """Binary Search Tree class"""
    def __init__(self):
        self.root = None


    def contains_helper(self, node, sought):
        if not node:
            return False
        if node.data == sought:
            return True

        if sought > node.data:
            # if node.right: # if the right node exists:
            return contains_helper(node.right, sought)
        elif sought < node.data:
            # if node.left:
            return contains_helper(node.left, sought)
        #return False



    
    def contains(self, sought):
        node = self.root
        return contains_helper(node, sought) # why don't helper functions need self?

    def adds_helper(self, node, to_add): # need to check ; use the HB implementation below
        current_node = node # self is the tree, node should be root
            # first have base case
            # did not need lines 51-53 initially
            # if not current_node.next: # if a next node doesn't exist
            #     current_node.next = Node(new_data) # then we point the leaf node to new data
            #problem is that we may not only be inserting leaf nodes; there may be some in middle too
            # if current_node.next > new_data:

        if new_data > current_node.data: # if value within new_data larger than self.data
            if not current_node.right:
                current_node.next = Node(new_data)
            else:
                adds_helper(self, current_node.right, new_data)
        if new_data < current_node.data:
            if not current_node.left:
                current_node.next = Node(new_data)
            else:
                adds_helper(self, curent_node.left, new_data)

    def adds(self, to_add):
        node = self.root
        return adds_helper(node, to_add)
        

############### HB IMPLEMENTATION

    class Node(object):  # ...
        def insert(self, new_data):

            current_node = self
            # first have base case
            # did not need lines 51-53 initially
            # if not current_node.next: # if a next node doesn't exist
            #     current_node.next = Node(new_data) # then we point the leaf node to new data
            #problem is that we may not only be inserting leaf nodes; there may be some in middle too
            # if current_node.next > new_data:

            if new_data > current_node.data: # if value within new_data larger than self.data
                if not current_node.right:
                    current_node.next = Node(new_data)
                else:
                    insert(current_node.right, new_data)
            if new_data < current_node.data:
                if not current_node.left:
                    current_node.next = Node(new_data)
                else:
                    insert(curent_node.left, new_data)











        