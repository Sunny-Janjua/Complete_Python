print("Lambda, Filter, Map and Reduce")
print("Lambda")
print("A lambda function is an anonymous function (function without a name).")
print("Lambda functions can have any number of arguments but only one expression. The")
print("expression is evaluated and returned.")
print("We use lambda functions when we require a nameless function for a short period of time.")

print("Filter")
print("It is used to filter the iterables/sequence as per the conditions.")
print("Filter function filters the original iterable and passes the items that returns True for the function")
print("provided to filter.")
print("It is normally used with Lambda functions to filter list, tuple, or sets.")
print("filter() method takes two parameters:")
print("function - function tests if elements of an iterable returns true or false")
print("iterable - Sequence which needs to be filtered, could be sets, lists, tuples, or any iterators")

print("Map")
print("The map() function applies a given function to each item of an iterable (list, tuple etc.) and")
print("returns a list of the results.")
print("map() function takes two Parameters :")
print("function : The function to execute for each item of given iterable.")
print("iterable : It is a iterable which is to be mapped.")
print("Returns : Returns a list of the results after applying the given function to each item of a given")
print("iterable (list, tuple etc.)")

print("Reduce")
print("The reduce() function is defined in the functools python module.The reduce() function")
print("receives two arguments, a function and an iterable. However, it doesn't return another iterable,")
print("instead it returns a single value.")
print("Working:")
print("1) Apply a function to the first two items in an iterable and generate a partial result.")
print("2) The function is then called again with the result obtained in step 1 and the next value in the")
print("sequence. This process keeps on repeating until there are items in the sequence.")
print("3) The final returned result is returned and printed on console.")

addition=lambda number1,number2:number1+number2
print(addition(2,3))

addition = lambda a : a + 10 # This lambda function adds value 10 to an argument
print(addition(5))

product = lambda a, b : a * b #This lambda function takes two arguments (a,b) and
print(product(5, 6))


res = (lambda *args: sum(args)) # This lambda function can take any number of ar
print(res(10,20))
print(res(10,20,30,40))
print(res(10,20,30,40,50,60,70))


addition = lambda a, b, c : a + b + c #This lambda function takes three argument
print(addition(5, 6, 2))

kwgs=(lambda **kwargs:sum(kwargs.values()))
print(kwgs(a=44,b=434))


res1 = (lambda **kwargs: sum(kwargs.values()))
res1(a = 10 , b= 20 , c = 30) , res1(a = 10 , b= 20 , c = 30, d = 40 , e = 50)


def product(nums):
 total = 1
 for i in nums:
    total *= i
 return total
print(product([1,2,3,4,5,6]))


# This lambda function can take any number of arguments and return thier product.
res1 = (lambda **kwargs: product(kwargs.values()))
print(res1(a = 10 , b= 20 , c = 30) , res1(a = 10 , b= 20 , c = 30, d = 40 , e = 50))


def myfunc(n):
 return lambda a : a + n
add10 = myfunc(10)
add20 = myfunc(20)
add30 = myfunc(30)
print(add10(5))
print(add20(5))
print(add30(5))


list1 = [1,2,3,4,5,6,7,8,9]
odd_num = list(filter(lambda n: n%2 ==1 ,list1))
print(odd_num)

def twice(n):
 return n*2

doubles = list(map(twice,odd_num))
print(doubles)

doubles = list(map(lambda n:n*2,odd_num)) 
print(doubles)