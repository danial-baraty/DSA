"""
Memory behavior explanation:

1. Before any function call:
   - Global frame (main stack) exists.
   - 'a' and 'b' references exist in global frame.
   - Objects:
       a -> int(5) on heap
       b -> list [1, 2, 3] on heap
   - func stack frame does not exist yet.

2. During func() execution:
   - A new stack frame for func() is created.
   - Local references inside func() are created on func's stack frame:
       x -> int(10) on heap
       y -> list [4, 5] on heap
   - Both references live only in func's stack frame.
   - Heap objects exist as long as there is a reference to them.

3. After func() returns:
   - func's stack frame is destroyed.
   - References x and y are gone.
   - Heap objects int(10) and list [4,5] have no references now.
     -> Eligible for garbage collection.
   - Global references a and b still exist, so their objects remain on heap.
"""

# main-level variables
a = 5          # integer object on heap, 'a' reference stored in global frame (main stack)
b = [1, 2, 3]  # list object on heap, 'b' reference stored in global frame (main stack)

def func():
    # Stack frame for func is created here
    x = 10     # integer object on heap, 'x' reference on func stack
    y = [4, 5] # list object on heap, 'y' reference on func stack
    print("Inside func:", x, y)
    # When func ends, stack frame is destroyed. x and y references gone.

print("Main-level variables:", a, b)
func()
# After func() call:
# - func's stack frame removed
# - x and y references no longer exist
# - Heap objects they pointed to are garbage collected if no other references
# - a and b still exist in global frame, so their heap objects remain
