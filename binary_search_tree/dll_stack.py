import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


# stack is LIFO (Last In First Off)
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # We've already added all the functionality necessary for Stack to operate
        self.storage = DoublyLinkedList()

    def push(self, value):
        # pushes to head
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        # removes from head
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return

    def len(self):
        return self.size
