
class Node:
    """Represents a single node in a linked list."""

    def __init__(self, info):
        """Initialize a node with data and a pointer to the next node."""
        self.info = info
        self.next = None


class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        """
        Initialize an empty linked list.
        `first` points to the head node, `last` to the tail node.
        """
        self.first = None
        self.last = None
    
    def append(self, x):
        """Add a new node with value `x` at the end of the list."""
        new_node = Node(x)

        if not self.first:
            # List is empty → first and last point to the new node
            self.first = new_node
            self.last = new_node
        else:
            # Link the last node to the new one and update `last`
            self.last.next = new_node
            self.last = new_node

    def show(self):
        """
        Return a list of all node values in order.
        If empty, return None.
        """
        if not self.first:
            return None
        
        items = []  # Store all node data
        ptr = self.first
        while ptr:
            items.append(ptr.info)
            ptr = ptr.next
        return items
