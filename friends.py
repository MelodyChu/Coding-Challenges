"""Find whether two people in an undirected graph are friends.

Let's create a graph and add a bunch of people:

    >>> f = FriendGraph()
    >>> f.add_person("Frodo")
    >>> f.add_person("Sam")
    >>> f.add_person("Gandalf")
    >>> f.add_person("Merry")
    >>> f.add_person("Pippin")
    >>> f.add_person("Treebeard")
    >>> f.add_person("Sauron")
    >>> f.add_person("Dick Cheney")

Now, let's set some friendships:

    >>> f.set_friends("Frodo", ["Sam", "Gandalf", "Merry", "Pippin"])
    >>> f.set_friends("Sam", ["Merry", "Pippin", "Gandalf"])
    >>> f.set_friends("Merry", ["Pippin", "Treebeard"])
    >>> f.set_friends("Pippin", ["Treebeard"])
    >>> f.set_friends("Sauron", ["Dick Cheney"])

We specifically said Sam was a friend of Frodo's, so they should be
connected:

    >>> f.are_connected("Frodo", "Sam")
    True

Our ``set_friends()`` sets the reciprocal relationship automatically
(this is an "undirected graph"), so Sam is also friends with Frodo:

    >>> f.are_connected("Sam", "Frodo")
    True

Sam isn't friends with Treebeard -- but we can find a connection
(Sam -> Frodo -> {Merry or Pippin} -> Treebeard)

    >>> f.are_connected("Sam", "Treebeard")
    True

Poor Sauron. He won't be invited to Frodo's tea party:

    >>> f.are_connected("Frodo", "Sauron")
    False

He does have friends of his own, though:

    >>> f.are_connected("Sauron", "Dick Cheney")
    True

Joel Burton <joel@joelburton.com>
"""


class PersonNode(object):
    """A node in a graph representing a person.

    This is created with a name and, optionally, a list of adjacent nodes.
    """

    def __init__(self, name, adjacent=[]):
        self.name = name
        self.adjacent = set(adjacent)

    def __repr__(self):
        return "<PersonNode %s>" % self.name


class FriendGraph(object):
    """Graph to keep track of social connections."""

    def __init__(self):
        """Create an empty graph.

        We keep a dictionary to map people's names -> nodes.
        """

        self.nodes = {} #initialize as empty dict

    def add_person(self, name):
        """Add a person to our graph.

            >>> f = FriendGraph()
            >>> f.nodes
            {}

            >>> f.add_person("Dumbledore")
            >>> f.nodes
            {'Dumbledore': <PersonNode Dumbledore>}
        """

        if name not in self.nodes:
            # Be careful not to just add them a second time -- otherwise,
            # if we accidentally added someone twice, we'd clear our their list
            # of friends!
            self.nodes[name] = PersonNode(name) # make name key; node itself if the value

    def set_friends(self, name, friend_names):
        """Set two people as friends.

        This is reciprocal: so if Romeo is friends with Juliet, she's
        friends with Romeo (our graph is "undirected").

        >>> f = FriendGraph()
        >>> f.add_person("Romeo")
        >>> f.add_person("Juliet")
        >>> f.set_friends("Romeo", ["Juliet"])

        >>> f.nodes["Romeo"].adjacent
        set([<PersonNode Juliet>])

        >>> f.nodes["Juliet"].adjacent
        set([<PersonNode Romeo>])
        """

        person = self.nodes[name]

        for friend_name in friend_names:
            friend = self.nodes[friend_name]

            # Since adjacent is a set, we don't care if we're adding duplicates ---
            # it will only keep track of each relationship once. We do want to
            # make sure that we're adding both directions for the relationship.
            person.adjacent.add(friend)
            friend.adjacent.add(person)

    # def are_connected(self, name1, name2): # self is the friend graph
    #     """Is this name1 friends with name2?"""
    #     """Issue with this implementation is that it's not checking for dupes in friend_queue """
    #     #current = name1
    #     friend_queue = [name1] #using as a stack

    #     while friend_queue:
    #         connection = friend_queue.pop()
    #         friend_queue.extend(connection.adjacent)
    #         for friend in friend_queue:
    #             if friend == name2:
    #                 return True
    #     return False
    # try # 2
    # def are_connected(self, name1, name2):
    #     """starting with HB sample code"""
    #     person1 = self.nodes[name1]
    #     person2 = self.nodes[name2]

    #     to_visit = []
    #     to_visit.append(person1)
    #     seen = set()
    #     seen.add(person1)

    #     while to_visit:
    #         node = to_visit.pop(0) #or is it dequeue?
    #         for friend in node.adjacent:
    #             if friend not in seen:
    #                 to_visit.append(friend)
    #                 seen.add(friend)
    #             if friend == person2:
    #                 return True
    #     return False # if Queue is empty and still not found


    def are_conected(self, name1, name2, seen=set()):
        person1 = self.nodes[name1] # this will update
        person2 = self.nodes[name2]
        if person1 == person2:
            return True
        else:
            #seen.add(person1.adjacent) # add people to the seen
            for friend in person1.adjacent:
                if friend not in seen:
                    seen.add(friend)
                    self.are_connected(friend.name, name2, seen) # not sure waht to do w/ this line
        return False
                


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
