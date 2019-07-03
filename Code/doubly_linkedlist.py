
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

        #self.tail = None
        #self.head = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class DoublyLinkedList(object):
    def append(self, item):
        new_node = Node(item)
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list."""
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        self.size += 1



    def find():
        pass

    def delete():
        pass
