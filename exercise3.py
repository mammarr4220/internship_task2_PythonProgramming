# Exercise 3.1

# Through the for loop, i includes values ranging from 1 to 20. The if-else statements are conditionals that check if the numbers in the loop are divisible by 3 and 5 and print
# required result
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
# Exercise 3.2

even = 0 # Start with the value of even as 0

for i in range(1, 101):
    if i % 2 == 0: # Checks if the numbers are divisible by 2
        even += i # If the numbers are divisible, they are added together one by one as the loop continues
print(even)


print(sum([x for x in range(1, 101) if x % 2 == 0])) # List comprehension

# Exercise 3,3

words = ["hi", "hello", "hey", "howdy"]

uppercase_long_words = [word.upper() for word in words if len(word) > 3] # .upper() converts the words in the list to uppercase and a new list is created, which stores words with a
# length greater than 3

print(uppercase_long_words)