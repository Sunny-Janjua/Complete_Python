# Program 3
# Write a Python program to find the area of a triangle.

length=int(input("Enter your Area of length : "))
width=int(input("Enter your Area of width : "))

def area(l,w):
    area=l*w
    return area

area_of_triangle=area(length,width)
print(f"area_of_triangle : {area_of_triangle}")

# Input the base and height from the user
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
# Calculate the area of the triangle
area = 0.5 * base * height
# Display the result
print(f"The area of the triangle is: {area}")


# Program 4
# Write a Python program to swap two variables.

a=int(input("Enter your first value : "))
b=int(input("Enter your first value : "))
print("With out swape value")
print(a)
print(b)

tem=0
tem=a
a=b
b=tem

print("After swape value")
print(a)
print(b)

print("Swape value without add third variable!")

a=int(input("Enter your first value : "))
b=int(input("Enter your first value : "))
print("With out swape value")
print(a)
print(b)

a=a+b
b=a-b
a=a-b

print("After swape value")
print(a)
print(b)

# Input two variables
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
# Display the original values
print(f"Original values: a = {a}, b = {b}")
# Swap the values using a temporary variable
temp = a
a = b
b = temp
# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")
