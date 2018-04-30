"""Count employees in an org chart.

Our organization has the following org chart::

                    Jane
          Jessica          Janet
       Al  Bob  Jen     Nick  Nora
                                Henri

Let's make this chart::

    >>> henri = Node("Henri")
    >>> nora = Node("Nora", [henri])
    >>> nick = Node("Nick")
    >>> janet = Node("Janet", [nick, nora])
    >>> al = Node("Al")
    >>> bob = Node("Bob")
    >>> jen = Node("Jen")
    >>> jessica = Node("Jessica", [al, bob, jen])
    >>> jane = Node("Jane", [jessica, janet])

And test our counting function::

    >>> henri.count_employees()
    0

    >>> nora.count_employees()
    1

    >>> jane.count_employees()
    8

We provide a non-recursive version, let's make sure that gives the same
answer::

    >>> jane.count_employees_nonrecursive()
    8

"""


class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    # def count_employees(self, children): # dont need to pass children in
    #     to_visit = [self]
    #     children = self.children # should be a list
    #     if not children: # if current node doesn't have child
    #         return len(children) # return 0
    #     else: # if self.children exists: 
    #         #self.children.extend(self.children) # put children inside of children list
    #         next_child = children.pop(0) # pop first item from list
    #         #if next_child.children:
    #         children.extend(next_child.children)
    #         return self.count_employees(next_child, children) #how to make self become next_child? check: shouldn't need to return
    
    # def count_employees(self): # Better to use stack or queue?
    #     to_visit = [self]

    #     counter = 0 # initially; don't count the self

    #     while to_visit: # while there are people in stack
    #         next = to_visit.pop() # pop from back; depth first search
    #         counter += 1
    #         to_visit.extend(next.children)

    #     return counter - 1

    def count_employees(self): # return # of employees below node is self
        current = self
        counter = 0
        if len(current.children) == 0:
            return 0
        else:
            for child in current.children:
                #counter += len(current.children)
                counter += child.count_employees() + 1
            return counter 
            







        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.
        """


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE A TREE GENIUS!\n"

