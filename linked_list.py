
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

    def append_ordered(self, x):
        pass
    

    def remove_item(self, x):
        """
        Remove the first occurrence of item 'x' from the linked list.
        If the list is empty or item not found, return a message.
        """
        ptr = self.first   # Current node pointer
        prev = None        # Tracks previous node

        if not self.first:  # Case: list is empty
            return "List is empty"

        while ptr:
            if ptr.info != x:
                prev = ptr
                ptr = ptr.next
            else:
                if ptr == self.first:  # Case: remove first node
                    if ptr.next == None:  # Case: list has only one node
                        self.first = self.last = None
                        return
                    self.first = ptr.next
                    return
                
                elif ptr == self.last:  # Case: remove last node
                    prev.next = None
                    self.last = prev
                    return
                
                else:  # Case: remove middle node
                    prev.next = ptr.next
                    return

        return "Item not found"  # If loop finishes without finding 'x'


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
