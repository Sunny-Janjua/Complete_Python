print("Classes & Objects")


print('A Class is an object constructor or a "blueprint" for creating objects.')
print("Objects are nothing but an encapsulation of variables and functions into a single entity.")
print("Objects get their variables and functions from classes.")
print("To create a class we use the keyword class.")
print("The first string inside the class is called docstring which gives the brief description about the")
print("class.")
print("All classes have a function called which is always executed when the class is")
print("being initiated.")
print("We can use function to assign values to object properties or other operations")
print("that are necessary to perform when the object is being created")
print("The self parameter is a reference to the current instance of the class and is used to access")
print("class variables.")
print("self must be the first parameter of any function in the class")
print("The super() builtin function returns a temporary object of the superclass that allows us to")
print("access methods of the base class.")
print("super() allows us to avoid using the base class name explicitly and to enable multiple")
print("inheritance.")
print("The __init__() function is called automatically every time the class is being used to create a")


class parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

obj=parent("Asif", 25)
print("Called by name!")
print(obj.name)
print(obj.age)
print("Called by attribute!")
obj.show()

# Create a class with property "var1"
class myclass:
 var1 = 10

obj1 = myclass() # Create an object of class "myclass()"
print(obj1.var1) # Access the property "var1" using the object "obj1"



class emp():
    def __init__(self,name,age,email):
      self.name=name
      self.age=age
      self.email=email
    
    def print_value(self):
      print(f"Our emp name is {self.name} and age is {self.age} and email is {self.email}")
      
obj=emp("hussnain mulazam",45,"hussnainmulazam@gmail.com")
print(obj.name)
print(obj.age)
print(obj.email)
obj.print_value()

print("THIS IS MY EMPLOYEE CLASS !")

class Employee:
 def __init__(self, name, empid): 
    self.name = name
    self.empid = empid
 def greet(self):
    print("Thanks for joining ABC Company {}!!".format(self.name))
emp1 = Employee("Asif", 34163)
print('Name :- ',emp1.name)
print('Employee ID :- ',emp1.empid)
emp1.greet()


print("Inheritance")

print("Inheritance is a powerful feature in object oriented programming.")
print("Inheritance provides code reusability in the program because we can use an existing class")
print("(Super Class/ Parent Class / Base Class) to create a new class (Sub Class / Child Class /")
print("Derived Class) instead of creating it from scratch.")
print("The child class inherits data definitions and methods from the parent class which facilitates the")
print("reuse of features already available. The child class can add few more definitions or redefine a")
print("base class method.")
print("Inheritance comes into picture when a new class possesses the 'IS A' relationship with an")
print("existing class. E.g Student is a person. Hence person is the base class and student is derived")
print("class.")


class person: # Parent Class
 def __init__(self, name , age , gender):
    self.name = name
    self.age = age
    self.gender = gender

 def PersonInfo(self):
    print('Name :- {}'.format(self.name))
    print('Age :- {}'.format(self.age))
    print('Gender :- {}'.format(self.gender))



class student(person): # Child Class
 def __init__(self,name,age,gender,studentid,fees):
    person.__init__(self,name,age,gender)
    self.studentid = studentid
    self.fees = fees

 def StudentInfo(self):
    print('Student ID :- {}'.format(self.studentid))
    print('Fees :- {}'.format(self.fees))


class teacher(person): # Child Class
 def __init__(self,name,age,gender,empid,salary):
    person.__init__(self,name,age,gender)
    self.empid = empid
    self.salary = salary

 def TeacherInfo(self):
    print('Employee ID :- {}'.format(self.empid))
    print('Salary :- {}'.format(self.salary))

stud1 = student('Asif' , 24 , 'Male' , 123 , 1200)
print('Student Details')
print('---------------')
stud1.PersonInfo() # PersonInfo() method presnt in Parent Class will be access
stud1.StudentInfo()
print()
teacher1 = teacher('Basit' , 36 , 'Male' , 456 , 80000)
print('Employee Details')
print('---------------')
teacher1.PersonInfo() # PersonInfo() method presnt in Parent Class will be acc
teacher1.TeacherInfo()



class person: # Parent Class
 def __init__(self, name , age , gender):
    self.name = name
    self.age = age
    self.gender = gender

 def PersonInfo(self):
    print('Name :- {}'.format(self.name))
    print('Age :- {}'.format(self.age))
    print('Gender :- {}'.format(self.gender))



class student(person): # Child Class
 def __init__(self,name,age,gender,studentid,fees):
    person.__init__(self,name,age,gender)
    self.studentid = studentid
    self.fees = fees

 def StudentInfo(self):
    print('Student ID :- {}'.format(self.studentid))
    print('Fees :- {}'.format(self.fees))


stud1 = student('Asif' , 24 , 'Male' , 123 , 1200)
print('Student Details')
print('---------------')
stud1.PersonInfo() # PersonInfo() method presnt in Parent Class will be access
stud1.StudentInfo()
print()



# super() builtin function allows us to access methods of the base class.
print("super() builtin function allows us to access methods of the base class.")
class person: # Parent Class
 def __init__(self, name , age , gender):
    self.name = name
    self.age = age
    self.gender = gender

 def PersonInfo(self):
    print('Name :- {}'.format(self.name))
    print('Age :- {}'.format(self.age))
    print('Gender :- {}'.format(self.gender))



class student(person): # Child Class
 def __init__(self,name,age,gender,studentid,fees):
    super().__init__(name,age,gender)
    self.studentid = studentid
    self.fees = fees

 def StudentInfo(self):
    super().PersonInfo()
    print('Student ID :- {}'.format(self.studentid))
    print('Fees :- {}'.format(self.fees))

stud = student('Asif' , 24 , 'Male' , 123 , 1200)
print('Student Details')
print('---------------')
stud.StudentInfo()


print("Multi-level Inheritance")

print("In this type of inheritance, a class can inherit from a child class or derived class.")
print("Multilevel Inheritance can be of any depth in python")


class person: # Parent Class
 def __init__(self, name , age , gender):
    self.name = name
    self.age = age
    self.gender = gender

 def PersonInfo(self):
    print('Name :- {}'.format(self.name))
    print('Age :- {}'.format(self.age))
    print('Gender :- {}'.format(self.gender))



class employee(person): # Child Class
 def __init__(self,name,age,gender,empid,salary):
    person.__init__(self,name,age,gender)
    self.empid = empid
    self.salary = salary

 def employeeInfo(self):
    print('Employee ID :- {}'.format(self.empid))
    print('Salary :- {}'.format(self.salary))



class fulltime(employee): # Grand Child Class
 def __init__(self,name,age,gender,empid,salary,WorkExperience):
    employee.__init__(self,name,age,gender,empid,salary)
    self.WorkExperience = WorkExperience

 def FulltimeInfo(self):
    print('Work Experience :- {}'.format(self.WorkExperience))



class contractual(employee): # Grand Child Class
 def __init__(self,name,age,gender,empid,salary,ContractExpiry):
    employee.__init__(self,name,age,gender,empid,salary)
    self.ContractExpiry = ContractExpiry

 def ContractInfo(self):
    print('Contract Expiry :- {}'.format(self.ContractExpiry))

print('Contractual Employee Details')
print('****************************')
contract1 = contractual('Basit' , 36 , 'Male' , 456 , 80000,'21-12-2021')
contract1.PersonInfo()
contract1.employeeInfo()
contract1.ContractInfo()
print('\n \n')
print('Fulltime Employee Details')
print('****************************')
fulltim1= fulltime('Asif' , 22 , 'Male' , 567 , 70000, 12)
fulltim1.PersonInfo()
fulltim1.employeeInfo()
fulltim1.FulltimeInfo()



print("Multiple Inheritance")

print("Multiple inheritance is a feature in which a class (derived class) can inherit attributes and")
print("methods from more than one parent class.")
print("The derived class inherits all the features of the base case.")


class parant:
  def __init__(self,name,age,roll_no,email):
    self.name=name
    self.age=age
    self.roll_no=roll_no
    self.email=email

  def print_values(self):
    print(f"My name is : {self.name}")
    print(f"My name is : {self.age}")
    print(f"My name is : {self.roll_no}")
    print(f"My name is : {self.email}")

obj=parant("sunny janjua",444,4455,"hussnainmulazam@gmail.com")
print(obj.name)
print(obj.age)
print(obj.roll_no)
print(obj.email)

obj.print_values()



class Date:
 def __init__(self,date):
    self.date = date

class Time:
 def __init__(self,time):
    self.time = time
# class timestamp(CurrentDate,CurrentTime):
 def __init__(self,date,time):
    # CurrentDate.__init__(self,date)
    # CurrentTime.__init__(self,time)
    DateTime = self.date + ' ' + self.time
    print(DateTime)
# datetime1 = timestamp( '2020-08-09', '23:48:55')
# print(datetime1)