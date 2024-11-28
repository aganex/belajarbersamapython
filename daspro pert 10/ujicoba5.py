# Global variable

# Defining the function
def sum(arg1, arg2):
    """Adds variables and returns the result."""
    total = arg1 + arg2;
    # total is a local variable here
    print("Inside the function, the value of total:", total)
    return total

# Calling the sum function
sum(10, 20)

print("Outside the function, the value of total:", total) 