# This code demonstrates the different scopes in Python: 
# Built-in, Global, Local, and Enclosing (LEGB rule).


# ------------------- Built-in Scope -------------------
# Built-in functions like 'len()' are always available in Python.

def example_builtin():
    numbers = [1, 2, 3]
    print(len(numbers))  # Accessing built-in function 'len'

example_builtin()


# ------------------- Global Scope -------------------
# Global variables are defined at the top-level of the file and can be accessed throughout the file.

global_var = "I am global"

def example_global():
    # Accessing a variable from the global scope
    print(global_var)  # Accessible from global scope

example_global()

# Accessing a variable from the global scope
print(global_var)  # This will print "I am global"


# ------------------- Local Scope -------------------
# Local variables are only accessible within the function they are defined in.

def example_local():
    local_var = "I am local"
    print(local_var)  # Accessible only within this function

example_local()

# The print statement above can only be executed by calling the function.
# print(local_var)  will raise a NameError because 'local_var' is not accessible outside the function.



# ------------------- Enclosing Scope -------------------
# Enclosing variables are accessible from inner functions defined within outer functions.

def outer_function():
    enclosing_var = "I am enclosing"
    
    def inner_function():
        # Accessing a variable from the enclosing function's scope
        print(enclosing_var)  # Accessible from enclosing scope

    inner_function()

outer_function()
