
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class Doubly_LinkedList(object):
    def append(item):
        new_node = Node(item)
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    def prepend():
        pass

    def find():
        pass

    def delete():
        pass
