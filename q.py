
class Node:
    def __init__(self, info):
        self.info = info          # Data stored in the node
        self.next = None          # Reference to the next node

class Q:
    def __init__(self):
        self.first = None         # Front of the queue
        self.last = None          # End of the queue

    def enqueue(self, info):
        """
        Add an item to the end of the queue.
        """
        new_node = Node(info)

        if not self.first:         # If queue is empty, new node is both first and last
            self.first = new_node
            self.last = new_node
            return
        
        self.last.next = new_node  # Link new node after the last node
        self.last = new_node       # Update last pointer
        return
    
    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        Raises IndexError if the queue is empty.
        """
        value = None
        
        if self.first:
            if not self.first.next:    # Only one node in the queue
                value = self.first.info
                self.first = self.last = None  # Reset pointers when queue becomes empty
                return value
        
            value = self.first.info
            self.first = self.first.next   # Move front pointer to next node
            return value
        
        raise IndexError("Dequeue from an empty queue!")  # Error when queue is empty
