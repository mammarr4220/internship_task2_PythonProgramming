# Exercise 5.1

letters = ["a", "b", "c"]
iterator = iter(letters) # iter() is used to create an iterator for the letters list

# Iterators move one by one, so the print(next(iterator)) prints the list values one by one, until the fourth call.
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) # On the fourth call, the terminal shows a StopIterator error, since there is no fourth element in the list.


# Exercise 5.2

letters = ["a", "b", "c"]
iterator = iter(letters)

# With the while loop, the iterator runs without having to repeat the print function multiple times. Through try-except, it runs, until the fourth call (the point where it receives
# a stop iteration error and breaks the loop)
while True:
    try:
        letter = next(iterator)
        print(letter)
    except StopIteration:
        break