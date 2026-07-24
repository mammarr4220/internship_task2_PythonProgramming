# Exercise 4.1

def is_even(n):
    return n %2 == 0 # Will return True or False depending if a number is even or not

# The function is called with 4 and 5 as arguments and the function is_even checks whether or not they are even
print(is_even(4)) 
print(is_even(5))


# Exercise 4.2
def greet(name, greeting="Hello"): # Takes name and greeting ("Hello" is the value of greeting) as parameters
    print(f"{greeting}, {name}!") # Returns the greeting and the name the user inputs

user_name = input("Enter your name: ") # Receives input from the user
greet(user_name) # Calls the greet function with user_name as the argument


# Exercise 4.3
def my_max(numbers):
    largest = numbers[0] # Takes the first value as largest

    for num in numbers:
        if num > largest: # Checks if the first value is smaller than a certain value
            largest = num # If true, the new num will be the largest number

    return largest # returns the largest number

print(my_max([1, 3, 5, 7, 8])) # A list of numbers is input as the argument for this function