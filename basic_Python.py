
# Variables and Data Types
integer_variable = 10
float_variable = 10.5
string_variable = "Hello, World!"
list_variable = [1, 2, 3, 4, 5]
dictionary_variable = {"name": "Sam", "age": 30}

# Printing variables
print("Integer:", integer_variable)
print("Float:", float_variable)
print("String:", string_variable)
print("List:", list_variable)
print("Dictionary:", dictionary_variable)

# If Statements
number = 10

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# For Loop
print("For Loop:")
for i in range(5):
    print(i)

# While Loop
print("While Loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# Functions and Modules

# Defining Functions
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# Using Functions
print(greet("Anish"))
print("Sum:", add(5, 3))

# Importing Modules
import math

# Using Functions from Imported Modules
print("Square root of 16 is:", math.sqrt(16))
print("Pi value is:", math.pi)

