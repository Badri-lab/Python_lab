OPEN Jupyter notebook from WSL Ubuntu 24.04 LTS application and copy its link with the token in the windows browser and keep working on it.
jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --port=8888

https://github.com/Abhiroyq1/eBooks-PDFs-necessary-for-data-analysis-by-Python-R-/blob/master/Image%20Preprocessing%20for%20Improving%20OCR%20Accuracy.pdf
https://github.com/b09/c_resources/tree/master

Julia: installation in WSL and Jupyter notebook setup: https://olejorik.github.io/post/juliawsl/

#PDBC to execute a DML statement
import oracledb  # dsn_tns = oracledb.makedsn('localhost', '1521', service_name='freepdb1')
try:
    connection = oracledb.connect(user='scott', password='tiger', dsn=(oracledb.makedsn('localhost', '1521', service_name='freepdb1')))
    cursor = connection.cursor()
    cursor.execute("update dept set deptno=deptno") #rowcount = cursor.rowcount
    print(f"Number of rows affected by the DML statement: {cursor.rowcount}")
    connection.commit()
except oracledb.DatabaseError as e:  print("There is a problem with Oracle", e)
finally:
    if cursor:  cursor.close()
    if connection:  connection.close()

#PDBC to run a SELECT query and fetch its results
import oracledb  # dsn_tns = oracledb.makedsn('localhost', '1521', service_name='freepdb1')
try:
    connection = oracledb.connect(user='scott', password='tiger', dsn=(oracledb.makedsn('localhost', '1521', service_name='freepdb1')))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM emp")
    for row in cursor.fetchall(): print(row)
except oracledb.DatabaseError as e:  print("There is a problem with Oracle", e)
finally:
    if cursor:  cursor.close()
    if connection:  connection.close()
# # Decorators - smart div which swaps the numbers if numerator is less than denominator
# def smart_div(func):
#     def inner(n, d):
#         if n < d:
#             n, d = d, n
#         func(n, d)
#
#     return inner
#
#
# @smart_div
# def div(x, y):
#     print(x / y)
#
#
# #div = smart_div(div)
# div(4, 2)
# div(2, 4)

# Decorators
# def f1(fn):
#     def f2():
#         print("Starting...")
#         fn()
#         print("Completed.")
#
#     return f2
#
#
# @f1
# def f():
#     print("Hello")
#
#
# # f = f1(f) #method 1: call without decorators
# f()

# # generator for infinite fibonacci series
# def fibo():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# x = fibo()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# generator function for generating square numbers
# def f():
#     for i in range(11):
#         sq = i * i
#         yield sq
#
#
# v = f()
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))

# for i in v:
#     print(i)


# Palindrome check
# def palindrome(s):
# method 1
# if s == s[::-1]:
#     return True
# else:
#     return False

# method 2
#     mid = len(s) // 2
#     n = len(s)-1
#     #print(mid)
#     for i in range(mid):
#         if s[i] == s[n - i]:
#             print(f"{s[i]} from position {i} matched with {s[n - i]} in position {n - i}")
#         else:
#             print(f"{s[i]} from position {i} did not match with {s[n - i]} in position {n - i}")
#             return False
#     return True
#
#
# str = input("Please enter some string for palindrome check: ")
# if palindrome(str):
#     print("It is a palindrome!")
# else:
#     print("Its not a palindrome, please try another string.")

# Sorting numbers(command line arguments) in ascending order
# from sys import argv
#
#
# def sort(l):
#     if len(l) < 2:
#         print("You must enter at least 2 numbers.")
#     else:
#         for i in range(len(l)):
#             for j in range(i + 1, len(l)):
#                 if l[i] > l[j]:
#                     t = l[i]
#                     l[i] = l[j]
#                     l[j] = t
#     return l
#
#
# print(f"Sorted order of the given numbers is as follows: {[x for x in sort(argv[1:])]}")

# Factorial using recursion
# def fact(n):
#     if n <= 1:
#         return n
#     else:
#         return n * fact(n - 1)
#
#
# num = int(input("What number you want to know factorial: "))
# print(f"Factorial of {num} is {fact(num)}")

# Fibonacci series using recursion
# def f(terms: int) -> int:
#     if terms <= 1:
#         return terms
#     else:
#         return f(terms - 1) + f(terms - 2)
#
#
# n = int(input("Please enter how many terms to generate: "))
# if n <= 0:
#     print("Please enter a positive integer.")
# else:
#     for i in range(n):
#         print(f(i), end=' ')

# writing and reading CSV file
# import csv
#
# data = [
#     ["Name", "Age", "City"],
#     ["John", 30, "New York"],
#     ["Alice", 25, "Los Angeles"],
#     ["Bob", 35, "Chicago"]
# ]
# with open("C:\\Users\\badri\\OneDrive\\Desktop\\py_file.csv", "w", newline="") as csvw:
#     w = csv.writer(csvw)
#     w.writerows(data)
#
# with open("C:\\Users\\badri\\OneDrive\\Desktop\\py_file.csv", "r", newline="") as csvr:
#     # r = csv.reader(csvr)
#     # for line in r:
#     #     print(line)
#     [print(line) for line in csv.reader(csvr)]

# Writing and Reading normal text file
# with open("C:\\Users\\badri\\OneDrive\\Desktop\\py_file.txt", "w") as fw:
#     fw.write("This is the first file i created from the python program!! Hope it worked and file got created!")
#     print("File created successfully!")
#
# with open("C:\\Users\\badri\\OneDrive\\Desktop\\py_file.txt", "r") as fr:
#     d = fr.read()
#     print("Able to read the file contents: ", d)


# from IPython.display import display
# import pandas as pd
#
# # creating a DataFrame
# dict = {'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
#         'Maths': [87, 91, 97, 95],
#         'Science': [83, 99, 84, 76]}
# df = pd.DataFrame(dict)
#
# # displaying the DataFrame
# display(df)

# from tabulate import tabulate
# import pandas as pd
#
# # creating a DataFrame
# dict1 = {'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
#         'Maths': [87, 91, 97, 95],
#         'Science': [83, 99, 84, 76]}
# df = pd.DataFrame(dict1)
#
# # displaying the DataFrame
# print(tabulate(df, headers='keys', tablefmt='psql'))

# import traceback
#
# def example_function():
#     try:
#         # Cause an exception
#         1 / 0
#     except Exception as e:
#         # Extract and print detailed information about the exception
#         print("Exception Type:", type(e).__name__)
#         print("Exception Message:", str(e))
#         print("Traceback:")
#         traceback.print_exc()
#
# if __name__ == "__main__":
#     example_function()


# Partial functions
# from functools import partial
#
#
# # A normal function
# def f(a, b, c, x):
#     return 1000 * a + 100 * b + 10 * c + x
#
#
# # A partial function that calls f with
# # a as 3, b as 1 and c as 4.
# g = partial(f,3,1,4)
#
# # Calling g()
# print(g(5))

# function(objects) as part of lists
# def greet(name):
#     return f"Hello, {name}!"
#
# function_list = [greet]   # we assign a list with single member greet to the variable function_list which is a list as per dynamic typing
# result = function_list[0]("Alice")  # Invoking the function using list and passing args. Result is "Hello, Alice!"
# print(result)

# nested functions, Closure: Function object that remembers values in the enclosing scope even if they are not present in memory
# from typing import Callable, Any
# def adder(n: int) -> Callable[[int], int]:
#     def inner(x: int,y: int) -> int:
#         return x * y + n
#     print(f"inner={inner}")
#     return inner
# # Create a function that adds 5 to its argument
# add_5 = adder(7)
# print(f"add_5={add_5}")
# # Use the returned function
# result1 = add_5(10,3) # 7 is remembered even after the adder call is completed in line 9
# print(f"result1={result1:3d}")  # Output: 37
#
# # Using another value for n
# add_10 = adder(12)
# result2 = add_10(10,9) # 12 is remembered even after the adder call is completed in line 16
# print(f"result2={result2:3d}")  # Output: 102

# def greet(name):
#     return f"Hello, {name}!"
#
#
# # Assigning a function to a variable
# greet_func = greet
# print(greet("test1"))
# print(greet_func("test2"))
#
#
# # Passing a function as an argument
# def apply(func, arg):
#     return func(arg)
#
#
# result = apply(greet, "Alice")
# print(result)
#
#
# # Returning a function from another function
# def create_greet_function():
#     def inner(name):
#         return f"Hello, {name}!"
#
#     return inner
#
#
# greet_func1 = create_greet_function()
# print(greet_func1("test3"))

# A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result.
# function arguments in python along with varying arguments to the function.
# Callable[..., Any] type hint provides flexibility for apply_function() to accept
# any function (func) and any arguments (args), and return any value.
# It reflects the dynamic nature of the function where the type of func
# and the types of its arguments and return value can vary.
# from typing import Callable, Any, Tuple
# def apply_function(func: Callable[..., Any], *args: Any) -> Any:  #higher order function
#     return func(*args)
# def square(x):
#     return x ** 2
# def cube(x):
#     return x ** 3
# def pow_n(x, y):
#     return x ** y
# # def apply_function(func, *value):  #higher order function
# #     return func(*value)
# result = apply_function(square, 5)
# print(result)  # Output: 25
# result = apply_function(cube, 5)
# print(result)  # Output: 125
# result = apply_function(pow_n, 5, 5)
# print(result)  # Output: 625

# python function dynamically accepting and returning varying arguments both
# positional and named using *args and **kwargs
# def return_dynamic_args(*args, **kwargs):
#     return args, kwargs
# def display_contents(data):
#     if isinstance(data, tuple):
#         if not data:
#             print("Tuple is empty")
#         else:
#             print("Tuple contents:")
#             for item in data:
#                 print(item)
#     elif isinstance(data, dict):
#         if not data:
#             print("Dictionary is empty")
#         else:
#             print("Dictionary contents:")
#             for key, value in data.items():
#                 print(f"{key}: {value}")
#     else:
#         print("Unsupported data type")
#
# # Example usage:
# result1 = return_dynamic_args()
# result2 = return_dynamic_args(1, 2, 3)
# result3 = return_dynamic_args(a=10, b=20, c=30)
# result4 = return_dynamic_args(1, 2, 3, a=10, b=20, c=30)
#
# display_contents(result1[0])
# display_contents(result1[1])
#
# display_contents(result2[0])
# display_contents(result2[1])
#
# display_contents(result3[0])
# display_contents(result3[1])
#
# display_contents(result4[0])
# display_contents(result4[1])


# python function accepting and returning multiple positional arguments dynamically using *args tuple
# def process_data(*args: tuple):
#     if len(args) == 0:
#         return None
#     elif len(args) == 1:
#         return args[0]
#     else:
#         return args
#
#
# def display_tuple_contents(tup: tuple) -> None:
#     if tup is None:
#         print("Tuple is empty")
#     elif isinstance(tup, tuple):
#         print("Tuple contents:")
#         for item in tup:
#             print(item)
#     else:
#         print(f"Tuple contents: {tup}")
#
#
# # Example 1: No arguments
# result1 = process_data()
# print("Result 1:", result1)  # Output will be None
# display_tuple_contents(result1)
#
# # Example 2: Single argument
# result2 = process_data(42)
# print("Result 2:", result2)  # Output will be 42
# display_tuple_contents(result2)
#
# # Example 3: Multiple arguments
# result3 = process_data(1, 2, 3, "hello")
# print("Result 3:", result3)  # Output will be (1, 2, 3, 'hello')
# display_tuple_contents(result3)

# multi threaded programming with different target functions different number of arguments
# from time import sleep, perf_counter
# from threading import Thread
# def f1(id):
#     print(f"Starting the task f1.")
#     sleep(id)
#     print(f"task f1 completed.")
# def f():
#     print(f"Starting the task f.")
#     sleep(5)
#     print(f"task f completed.")
# def f2(id1, id2):
#     print(f"Starting the task f2.")
#     sleep(id1 + id2)
#     print(f"task f2 completed.")
#
# start = perf_counter()
# t = Thread(target=f)
# t1 = Thread(target=f1, args=(3,))
# t2 = Thread(target=f2, args=(2, 5))
#
# t.start()
# t1.start()
# t2.start()
#
# t.join()
# t1.join()
# t2.join()
#
# end = perf_counter()
# print(f"It took {end - start:0.2f} seconds to complete.")

# multi threaded programming with same target function
# from time import sleep, perf_counter
# from threading import Thread
# def f(id):
#     print(f"Starting the task {id}.")
#     sleep(5)
#     print(f"task {id} completed.")
# start = perf_counter()
# threads = []
# for n in range(1, 4):
#     t = Thread(target=f, args=(n,))
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()
# end = perf_counter()
# print(f"It took {end - start:0.2f} seconds to complete.")

# superheroes = ["banana", "Orange", "Kiwi", "cherry"]
# print(f"Given order                           : {superheroes}")
# superheroes.reverse()
# print(f"List items in reverse order           : {superheroes}")
# superheroes.sort(reverse = True)
# print(f"Descending sort order                 : {superheroes}")
# superheroes.sort()
# print(f"Ascending sort order                  : {superheroes}")
# superheroes.sort(reverse=True,key=str.lower)
# print(f"Case-insensitive Descending sort order: {superheroes}")
# superheroes.sort(key=str.lower)
# print(f"Case-insensitive Ascending sort order : {superheroes}")

# for i in range(len(b)):
#     print(b[i])

# try:
#     s=["abcd123"]
#     s.remove("d")
#     print(s)
#     a=1/0
# except ZeroDivisionError as zde:
#     print(zde)
# except ValueError as ve:
#     print(ve)
# except IndexError as ie:
#     print(ie)

# list comprehension
# a = ["apple", "banana", "cherry", "kiwi", "mango"]
# b = [x if x != "banana" else "orange" for x in a]
# print(b)


# changing range of list items
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(str(a).ljust(30), len(a), sep="  |&|  ")
# a[3:5] = []
# print(str(a).ljust(30), len(a), sep="  |&|  ")


# list unpacking
# a = [("a", "b","c"), ("d","d", "f")]
# l1, l2 = a
# print(l1)
# print(l2)
# # print(l3)

# ternary operator
# a,b=10,2
# c=a**b if a<b else b-a
# print("c=",c)

# def f():
#     try:
#         None
#     except:
#         return "except"
#     else:
#         return "else"
#     # finally:
#     #     return "finally"
#
# print(f())
https://fte.mohan43u.space/#  => books on ML and DL in tamil by Nithya Duraisamy.

Python important points:

Difference between casefold() and lower()? Is there is anything similar available for uppercasing the string?
Difference between find() and index().


Topics to go through:

Generators- fibonacci series - 0 1 1 2 3 5 8 13 21 ...
# generator for infinite fibonacci series
def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


x = fibo()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# generator for fibonacci series with n terms
def fibo(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


x = fibo(15)
print(next(x))
print(next(x))
print(next(x))

Decorators
Sorting numbers in ascending or descending order
Palindrome check
Print all pairs with given sum
Fibonacci series using recursion
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


terms = int(input("How many terms: "))
if terms == 0:
    print("Please enter a positive integer.")
else:
    for i in range(terms):
        print(fibo(i), end=' ')
import sys, os, getopt
def main(argv):
 opts,args=getopt.getopt(argv,"i:")
 for o,a in opts:
  if o in "-i":
   run(a)
def run(a):
 inp_file=a+".cpp"
 exe_file=a+".exe"
 os.system("g++ "+inp_file+" -o "+exe_file)
 os.system(exe_file)
if __name__=="__main__":
 main(sys.argv[1:])
 

def f1():
 s=0
 for i in range(1000000000):
  s+=i
 return s

print(f1());


#include <iostream>
using namespace std;
int main(){
int i;
int s;
for(i=0;i<=1000000;i++) s+=i;
cout<<s<<endl;
return 0;
}


import sys
import Cython
import numpy as np
import subprocess, os
print("Python %d.%d.%d %s %s" % sys.version_info)
print("Cython %s" % Cython.__version__)
print("Numpy %s" % np.__version__)
print(subprocess.check_output([os.environ.get('CC','cc'),"--version"]).decode().splitlines()[0])
print([line for line in subprocess.check_output([os.environ.get('CC','cc'),"--version","-v"],stderr=subprocess.STDOUT).decode().splitlines() if ' version ' in line][0])

cdef int v1=100
print(v1)
cdef double v2
v2=2*v1
v2=<int>v2
print(v2)
