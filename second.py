#for loop, while loop in python

# for loop in lists 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#for loop in strings

for x in "banana":
  print(x)

#using break

fruit = ["apple", "banana", "cherry"]
for x in fruit:
  print(x)
  if x == "banana":
    break

#range function

for x in range(2, 30, 3): #starting,ending,step to increment
  print(x) 

#nested for loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 

#while loop

i = 1
while i < 6:
  print(i)
  i += 1

#break in while loop


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

#else statement

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#if else
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#short hand if
if a > b: print("a is greater than b")

#short hand if else
a = 2
b = 330
print("A") if a > b else print("B") 

#and / or

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#similarly or and not can be also used 


#match statement:The match statement is used to perform different actions based on different conditions.\

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

"""There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

#accesing list elements

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#replacing using range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#insert is used because it doesnot replace items but adds them
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append adds items at last
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#clear is used to empty the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#in descending sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#reverse the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 
