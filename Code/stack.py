#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    # I did this one
    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        if self.list.size == 0:
            return True
        return False

    # this one too
    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return self.list.size

    # and this
    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – we are only inserting one item at a KNOWN place"""
        # Push given item
        self.list.prepend(item)

    # and this
    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        if self.is_empty():
            print("list is empty")
            return None
        return self.list.head.data

    # me again
    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – we are removing one item at a KNOWN place"""
        # Remove and return top item, if any
        if self.is_empty():
            raise ValueError("this didnt work")

        top_item = self.list.head.data
        self.list.delete(top_item)
        # self.list.head = self.list.head.next
        # self.list.size -= -1
        return top_item


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – we are inserting one item at the top of the stack (a known place)"""
        # Insert given item
        self.list.append(item)
        return self

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is emp  diuty."""
        # Return top item, if any
        if self.is_empty():

            return None
        item_index = self.length() - 1
        return self.list[item_index]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – we are taking off one item at a given index place"""
        # Remove and return top item, if any
        if self.is_empty():

            raise ValueError("this list is empty")

        return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
