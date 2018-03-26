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
            
                
    
    
    