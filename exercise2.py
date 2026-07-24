# Exercise 2.1
colors = ["red", "green", "blue"]
colors.append("yellow") # Adds "yellow" to the end of the list
colors.insert(0, "black") # Adds "black at the beginning of the list (index 0)
print(len(colors)) # Prints as output the length of the colors list
print(colors[-1]) # Prints the last value in the colors list (since an index of -1 refers to the last value)

# Exercise 2.2
from collections import Counter

text = "the cat sat on the mat the cat purred"
length_count = dict(Counter(text.split())) # The sentence is split and Counter counts the amount of times a certain word appears and then dict converts it into a dictionary.

print(length_count)


# Exercise 2.3
nums = [4, 2, 7, 2, 9, 4, 4, 1]
setA = set(nums)  # Converts the nums list into a set
print(setA)


# Exercise 2.4

# a) Tuple ('tuple'), since for each RGB color, the value is a fixed set of three integers, which cannot be changed.

# b) Dictionary ('dict'), since every name (key) has a unique phone number (value).

# c) Set ('set'), since sets do not allow duplicate values (each value is unique).

# d) List ('list'), since lists are not organized in order.