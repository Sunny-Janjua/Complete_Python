# --- Variables and Data Types ---
age = 25  # int
height = 5.9  # float
name = "Alice"  # string
is_student = True  # bool

# --- List, Tuple, Dictionary, Set ---
my_list = [1, 2, 3, 4]  # List
my_tuple = (1, 2, 3)  # Tuple
my_dict = {'name': 'Alice', 'age': 25}  # Dictionary
my_set = {1, 2, 3}  # Set

# --- Operators ---
sum = age + 5  # Arithmetic
is_adult = age >= 18  # Comparison

# --- Conditional Statements ---
if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")

# --- Loops ---
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# --- Functions ---
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))

# --- File Handling ---
# Writing to a file
with open('file.txt', 'w') as f:
    f.write('Hello, Python!')

# Reading from a file
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

# --- Exception Handling ---
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    print("Finished.")

# --- List Comprehension ---
squares = [x**2 for x in range(10)]
print(squares)

# --- Lambda Function ---
square = lambda x: x**2
print(square(5))

# --- Generator Function ---
def my_gen():
    yield 1
    yield 2
    yield 3

for val in my_gen():
    print(val)

# --- Using Modules ---
import math
print(math.sqrt(16))  # Output: 4.0

# --- Simple Calculator Example ---
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

# Run the calculator
calculator()
