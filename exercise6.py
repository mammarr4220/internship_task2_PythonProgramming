# Exercise 6.1

def countdown(n):
    while n >= 1: # Loops down until n = 1
        yield n # The function pauses and outputs the current value
        n -= 1 # n decrements until it reaches 1
        
# The values are printed. The starting number (the argument of the function) is 5 and the last one will be 1
for value in countdown(5): 
    print(value)
    
# Exercise 6.2

def evens():
    current_value = 0 # Taking the starting value as 0
    # The while loop runs infinitely
    while True:
        yield current_value # Yields the current number and pauses
        current_value += 2 # Moves to the next number (skipping by 2)

# Initializing count for the number of items in a list
count = 0

# Goes through the values one by one
for value in evens():
    print(value)
    count += 1
    
# The loops breaks once count = 5
    if count == 5:
        break
    
# Exercise 6.3
square_list = [x * 2 for x in range(10)] # Takes x values ranging from 1-10 and prints out the values of x * 2 in list form
print(square_list)

# Through the list comprehension approach, the numbers appear in a list accurately. However, for the generator expression approach, it does not evaluate the values, as we have 
# not requested the values.
square_generator = (x**2 for x in range(10))
print(square_generator)