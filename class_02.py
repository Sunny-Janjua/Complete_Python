print("List is created in python")
import sys
import keyword

print(keyword.kwlist)
my_list=[]
print(my_list)
print(type(my_list))
print(sys.getsizeof(my_list))


list2 = [10,30,60] 
print(list2)


list3 = [10.77,30.66,60.89] 

print(list3)
list7 = ['Asif', 25 ,[50, 100],[150, 90] , {'John' , 'David'}]
print(list7)
print(len(list7))
list6 = [100, 'Asif', 17.765] 
print(list6)
list5 = ['Asif', 25 ,[50, 100],[150, 90]] 
print(list5)
list3 = [10.77,30.66,60.89] 
print(list3)

print("SLICING LIST IN PYTHON!")

mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
print(mylist)
print(mylist[2:5])
print(mylist[2:])
print(mylist[:5])
print(mylist[:])

print("APPENDING AND CHANGIN LIST  IN PYTHON USIGN DIFFERNENT METHOD OF PYTHON!")

mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
print(mylist)
mylist.append("nine")
print(mylist)
mylist.insert(4,"hussnainmulazam@gmail.com")
print(mylist)

mylist.insert(9,'ten') # Add item at index location 9
print(mylist)
mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
for i in mylist:
    print(i)

mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
mylist.pop()
print(mylist)

mylist.pop(5)
print(mylist)

mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
# del mylist 
# del is working but show errror for next statement so i cannot use it!
print(mylist)


mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
mylist.clear()
print(mylist)

mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
my_newlist=mylist.copy()
print(mylist)
print(id(mylist))
print(my_newlist)
print(id(my_newlist))

my_newlist[5]="hello world"
print(mylist)
print(my_newlist)

print("ADD TO LIST AND SHOW SINGLE LIST !")

list1 = ['one', 'two', 'three', 'four']
list2 = ['five', 'six', 'seven', 'eight']

print(list1+list2)

print(list1.extend(list2))

if 'eleven' in list1: # Check if 'eleven' exist in the list
 print('eleven is present in the list')
else:
 print('eleven is not present in the list')


mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
print(mylist)
mylist.reverse()
print(mylist)
mylist.reverse()
print(mylist)


mylist3 = [9,5,2,99,12,88,34]
mylist3.sort() # Sort list in ascending order
print(mylist3)
print("Sort list in ascending order")
mylist3 = [9,5,2,99,12,88,34]
mylist3.sort(reverse=True) # Sort list in ascending order
print(mylist3)

mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
for i in enumerate(mylist):
  print(i)


# All / Any
# True - If all elements in a list are true
# False - If any element in a list is false

L1 = [1,2,3,4,0]
print(all(L1))
print(any(L1))

mystring = "WELCOME"
mylist = [ i for i in mystring ] # Iterating through a string Using List Comprehe
print(mylist)

print("SHORT FORM TO DECLEAR FOR LOOP IN PYTHON!")
print("MOSTLY USE IN TUPLE LIST AND DICT AND SET!")

my_list="code with sunny janjua!"
new_list=[i for i in my_list]
print(new_list)


mylist1 = [ i for i in range(40) if i % 2 == 0] # Display all even numbers betwee
print(mylist1)


my_new_list=[i for i in range(100) if i % 2 == 0]
print(my_new_list)

my_list=[number*5 for number in range(10) if number%2==0]
print("Evenv number is printed!")
print(my_list)



list1 = [2,3,4,5,6,7,8]
list1 = [i*10 for i in list1]
print(list1)


#List all numbers divisible by 3 , 9 & 12 using nested "if" with List Comprehensi
mylist4 = [i for i in range(200) if i % 3 == 0 if i % 9 == 0 if i % 12 == 0]
print(mylist4)


mystr = "One 1 two 2 three 3 four 4 five 5 six 6789"
numbers = [i for i in mystr if i.isdigit()]
print(numbers)