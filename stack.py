
class Node:
    def __init__(self, info):
        self.info = info  # Data held by the node
        self.next = None  # Pointer to the next node

class Stack:
    def __init__(self):
        self.top = None  # Top node of the stack

    def push(self, info):
        """
        Add an item to the top of the stack.
        """
        new_node = Node(info)

        if not self.top:  # If stack is empty, new node becomes top
            self.top = new_node
            return
        
        new_node.next = self.top  # Link new node to current top
        self.top = new_node       # Update top pointer to new node

    def pop(self):
        """
        Remove and return the top item from the stack.
        Raises IndexError if stack is empty.
        """
        if self.top:
            value = self.top.info  # Store top value
            
            if not self.top.next:  # If only one node in stack
                self.top = None
                return value
            
            self.top = self.top.next  # Move top pointer to next item
            return value
        
        raise IndexError("Pop from an empty stack!")  # Stack empty error
