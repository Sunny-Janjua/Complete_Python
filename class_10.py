print("Method Overriding")

print("Overriding is a very important part of object oreinted programming because it makes")
print("inheritance exploit its full power.")
print("Overriding is the ability of a class (Sub Class / Child Class / Derived Class) to change the")
print("implementation of a method provided by one of its parent classes.")
print("When a method in a subclass has the same name, same parameter and same return type as")
print("a method in its super-class, then the method in the subclass is said to override the method in")
print("the super-class.")
print("The version of a method that is executed will be determined by the object that is used to")
print("invoke it.")
print("If an object of a parent class is used to invoke the method, then the version in the parent class")
print("will be executed, but if an object of the subclass is used to invoke the method, then the")
print("version in the child class will be executed.")


class person: # Parent Class
 def __init__(self, name , age , gender):
    self.name = name
    self.age = age
    self.gender = gender

 def greet(self):
    print("Hello Person")



class student(person): # Child Class
 def __init__(self,name,age,gender,studentid,fees):
    person.__init__(self,name,age,gender)
    self.studentid = studentid
    self.fees = fees
 def greet(self):
    print("Hello Student")


stud = student('Gabriel' , 56 , 'Male' , 45 , 345678)
print(stud.age)
print(stud.name)
print(stud.gender)
print(stud.studentid)
stud.greet() # greet() method defined in subclass will be triggered as "stud" is
person1 = person('Gabriel' , 56 , 'Male')
print(person1.age)
print(person1.name)
print(person1.gender)
person1.greet() 

print("Container")

print("Containers are data structures that hold data values.")
print("They support membership tests which means we can check whether a value exists in the")
print("container or not.")
print("Generally containers provide a way to access the contained objects and to iterate over them.")
print("Examples of containers include tuple, list, set, dict, str")

print("Iterable & Iterator")

print("An iterable is an object that can be iterated upon. It can return an iterator object with the")
print("purpose of traversing through all the elements of an iterable.")
print("An iterable object implements __iter()__ which is expected to return an iterator object. The")
print("iterator object uses the __next()__ method. Every time next() is called next element in the")
print("iterator stream is returned. When there are no more elements available StopIteration")
print("exception is encountered. So any object that has a __next()__ method is called an iterator.")


mylist = ['Asif' , 'Basit' , 'John' , 'Michael']
list_iter = iter(mylist) # Create an iterator object using iter()
print(next(list_iter)) # return first element in the iterator stream
print(next(list_iter)) # return next element in the iterator stream
print(next(list_iter))
print(next(list_iter))

print("Decorator")
print("Decorator is very powerful and useful tool in Python as it allows us to wrap another function in")
print("order to extend the behavior of wrapped function without permanently modifying it.")
print("In Decorators functions are taken as the argument into another function and then called inside the wrapper function.")

print("Advantages -")
print("Logging & debugging")
print("Access control and authentication")


def subtract(num1 , num2):
 res = num1 - num2
 print('Result is :- ', res)

subtract(4,2)
subtract(2,4)

def sub_decorator(func):
 def wrapper(num1,num2):
    if num1 < num2:
        num1,num2 = num2,num1
        return func(num1,num2)
 return wrapper

sub = sub_decorator(subtract)
sub(2,4)

@sub_decorator
def subtract(num1 , num2):
 res = num1 - num2
 print('Result is :- ', res)
subtract(2,4)



print("File Management")

file_open=open("sunny.txt","r")
print(file_open.read())


print("Error & Exception Handling")

print("Python has many built-in exceptions (ArithmeticError, ZeroDivisionError, EOFError, IndexError,")
print("KeyError, SyntaxError, IndentationError, FileNotFoundError etc) that are raised when your")
print("program encounters an error.")
print("When the exception occurs Python interpreter stops the current process and passes it to the")
print("calling process until it is handled. If exception is not handled the program will crash.")
print("Exceptions in python can be handled using a try statement. The try block lets you test a block")
print("of code for errors.")
print("The block of code which can raise an exception is placed inside the try clause. The code that")
print("will handle the exceptions is written in the except clause.")
print("The finally code block will execute regardless of the result of the try and except blocks.")
print("We can also use the else keyword to define a block of code to be executed if no exceptions")
print("were raised.")
print("Python also allows us to create our own exceptions that can be raised from the program using")
print("the raise keyword and caught using the except clause. We can define what kind of error to")
print("raise, and the text to print to the user")


