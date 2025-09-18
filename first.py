#summary of all things learned in day 1 

"""
indentation is mandatory in python unlike other languages
python is case sensitive in terms of variables as 
a and A are different and 
age and Age are different 
"" and '' both are same and can be used to represent strings
variable name must start with letters or underscore only
and cannot contain space and - only alphabets, numbers and an underscore


this is example of multiline strings in python
"""
#printing
print("Hello, World")
x,y,z="gaurav","sandesh","puskar"
print(x+y+z)
a=b=c="Hello"
print(a,b,c)
fruits=["apple","banana"]
a,b=fruits
print(a,b)
print(type(fruits))


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)#here output is fantastic
"""
data types in python
int,float,complex
str
list,tuple,dict
bool
"""
x=5#is interger
x=5.5#is float
x=5+1j#is complex
x="hello"#is string
x = ["apple", "banana", "cherry"]#list
x = {"apple", "banana", "cherry"}#set
x = ("apple", "banana", "cherry")#tuple
x={"name":"sandesh","age":20}#dict
print(x)
#generating random number
import random
print(random.randrange(1,9))
print("hello i am 'sandesh'")
for x in "banana":
  print(x)
  txt = "The best things in life are free!"
print("free" in txt)
vara = "The best things in life are free!"
if "expensive" not in vara:
     print("No, 'expensive' is NOT present.")


a = "Hello, World!"
print(a.upper())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" like trim in js

a = "Hello, World!"
print(a.replace("H", "J"))

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)