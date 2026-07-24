# Exercise 1.1
name = input("What is your name? ")  # Receives input for name
age = input("How old are you? ") # Receives input for age
height = input("How tall are you (in meters)? ") # Receives input for height

print(f'{name} is {age} years old and is {height} meters tall.')  # f' prints the input value along with the rest of the print statement.

# Exercise 1.2

# a) Integer    b) Float.    c) String.      d) Boolean     e) None

a = 7
b = 7.0
c = "7"
d = True
e = None

# type() is used to check the data type of a particular value
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# Exercise 1.3

celsius_temperature = input("What is the temperature (in degrees Celsius)? ")  # Receives temperature (Celsius) input from user
fahrenheit_temperature = float(celsius_temperature) * 9/5 + 32  # The input is converted into a float before being computed using the Fahrenheit conversion formula
print(f'The temperature is {fahrenheit_temperature} degrees Fahrenheit.') # A print statement that outputs the Fahrenheit equivalent of the Celsius temperature.