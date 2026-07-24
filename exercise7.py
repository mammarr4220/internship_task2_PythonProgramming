# Exercise 7.1

# The run_twice function will accept the say_hi function as an argument
def run_twice(func):
    func()
    func()
    

def say_hi():
    print("hi")
    
# Calls the say_hi function through run_twice, which has the say_hi function as an argument
run_twice(say_hi)

# Exercise 7.2

def announce(func): # The announce decorator is a wrapper shell around any functions inside it
    def wrapper(*args, **kwargs):
        print("Calling...")
        result = func(*args, **kwargs) # Executes the original function
        print("Done!")
        return result # Returns the output
    return wrapper

# 'Add' is passed through the 'announce' wrapper
@announce
def add(a, b):
    return a + b

# 'Wrapper' is triggered when 'add' is called
total = add(3, 5)
print(f"Result: {total}")

# Exercise 7.3

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # The time library is used when execution time needs to be captured
        result = func(*args, **kwargs) 
        end_time = time.time() # The end time is captured
        elapsed_time = end_time - start_time 
        print(f"[{func.__name__}] took {elapsed_time:.4f} seconds to complete.") # Once the elapsed time is calculated, the system prints out the amount of time it took for the code execution.
        
        return result
    return wrapper

# Applying the main wrapper
@timer
def heavy_loop(limit):
    total = 0
    for i in range(limit):
        total += i
    return total

heavy_loop(5_000_000)

# Exercise 7.4

# This decorator will return "hello, ada" in uppercase ("HELLO, ADA"). That is done by defining a wrapper that calls the original function and applies the .upper() method to the result.