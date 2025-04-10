# Program 32
# Write a Python Program to find sum of array.

array=[1,2,3,4,5,6,7,8,9]
sum=0
for i in array:
    sum+=i
print(sum)
    
# Finding Sum of Array Using sum()
import math
arr = [1,2,3]
ans = math.fsum(arr)
print('Sum of the array is ', ans)


# Function to find the sum of elements in an array
def sum_of_array(arr):
 total = 0 # Initialize a variable to store the sum

 for element in arr:
    total += element # Add each element to the total

 return total
# Example usage:
array = [1, 2, 3]
result = sum_of_array(array)
print("Sum of the array:", result)


# Program 33
# Write a Python Program to find largest element in an array.

def find_largest_element(arr):
 if not arr:
    return "Array is empty"
 largest_element = arr[0]
 for element in arr:
    if element > largest_element:
        largest_element = element
 return largest_element
my_array = [10, 20, 30, 99]
result = find_largest_element(my_array)
print(f"The largest element in the array is: {result}")


def largest_ele(array):
   if not array:
      return "Please enter and array element's "
   largest_element=array[0]

   for element in array:
      if element > largest_element:
        largest_element = element
   return largest_element


array=[1,2,4,5,6,875,54,7,46,75,557,4,7,34,7]
lg_array=largest_ele(array)
print(f"largest element is {lg_array}")


# Program 46
# Write a Python program to print all happy numbers between 1 and 100.


my_happy_number = "54"  # Treat this as a string to check for digits

# Iterate over each digit in the entered number
def check_number_is_happy(number):
   for i in number:
      if i in my_happy_number:
         print(f"My happy number is found: {i}")
      else:
         print(f"My happy number is not found: {i}")

number = input("Enter your number: ")
print(check_number_is_happy(number))





      
   



