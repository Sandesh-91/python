# finding the shape of  a numpy array
# zero d array
# one-d array
# two-d array
# three-d array

# 0-d array

import numpy as np

array = np.array(66)
print(f"Array is {array}")
print(array.shape)  # shape of numpy array

# 1-d numpy array

arr_one = np.array([1, 2, 3])
print(arr_one)
print(arr_one.shape)  # shape of numpy array

# 2-d array

arr_two = np.array([[2, 3, 4], [5, 6, 7]])
print(arr_two)
print(arr_two.shape)  # shape

# 3-d array

arr_three = np.array([[[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print("\n", arr_three)
print(arr_three.shape)


# reshaping the numpy  array
# 1.reshaping 1d array to 2d array
# 2.reshaping(flattening) 3d to 1d array

arr_re = np.array([1, 2, 3, 4, 5, 6])
reshape_arr = arr_re.reshape(2, 3)
print(reshape_arr)

# 2

reshape_arr1 = reshape_arr.reshape(-1)
print("\n", reshape_arr1)

# iterating numpy array

# 1d array
for a in reshape_arr1:
    print(a)

# 2d array
for b in reshape_arr:
    print(b)

# 3d array
for c in arr_three:
    print(c)


# joining numpy arrays
# 1.using concatanate\
# 2.using stack

# 1

arr1 = np.array([1, 2, 3])
arr2 = np.array([3, 4, 5])
rearr12 = np.concatenate((arr1, arr2))
rear = np.vstack((arr1, arr2))  # along columns
print("vstack ", rear)
# dstack along height
print("dstack ", np.dstack((arr1, arr2)))
print("columnstack ", np.column_stack((arr1, arr2)))


print("1d", rearr12)

# 2

arr12 = np.array([[1, 2, 3], [2, 3, 4]])
arr23 = np.array([[1, 3, 5], [7, 9, 11]])
rearr123 = np.stack((arr12, arr23))
rearr1234 = np.hstack((arr12, arr23))  # along rows

print("2d", rearr123)
print("2d", rearr1234)


# array spliting

abc = np.array([1,2,3,4,5,3])
rearrange=np.array_split(abc,2)
print("Array1 = ",rearrange[0])
print("Array2 = ",rearrange[1])

deg=np.array([[1,2,3],[4,5,6]])
redeg=np.array_split(deg,2)
print("Array 2d = ",redeg[0])
print("Array 2d = ",redeg[1])

#search a numpy array for a value

print(np.where(abc ==3)) # at array([2,5])

#sorting an array

#1d
a=np.array([12,9,10,17])
print(np.sort(a))

#2d
c=np.array([[12,9,8],[0,2,7]])
print(np.sort(c))
print("c",np.repeat(c,3,axis=0))

#string array
b=np.array(['sandesh','gaurav','madam','puskar','aamon','aemon'])
print(np.sort(b))

#axis in numpy axis=0 is vertical axis and axis=1 is horizontal axis

#.min gives minimum value and .max gives maximum value in array

print(c.min())
print(a.min())
print(c.min(axis=0)) #vertical
print(c.min(axis=1)) #horizontal

#intersecting two arrays  result is in sorted form

e=np.array([12,3,2])
f=np.array([12,27,2])
print(np.intersect1d(e,f)) #common elements in arrays

#if there is no intersection between arrays ouput is []

#difference between arrays 

g=np.array([12,17,18,20,25,30])
h=np.array([12,17,19,20,35,30])
print(np.setdiff1d(g,h)) #performs A-B
print(np.setdiff1d(h,g)) #performs B-A

#arithmetic operations on numpy arrays
#sum 
#subtract
#multiply
#divide

#sum 

h=np.array([10,12,15,20,25])
i=np.array([15,20,25,30,35])
print(np.sum([h,i])) #whole sum
print("v",np.sum([h,i],axis=0)) #vertical sum 
print(np.sum([h,i],axis=1)) #horizontal sum
print('x',np.repeat(c,3,axis=1))

#subtract 

print(np.subtract(h,i)) #columnwise diff

#multiply 

print(np.multiply(h,i)) #columnwise multiply

#divide 

print(np.divide(i,h)) #divide i by h 

#scalar operations in numpy arrays

print(h+10,i+5)
#similary we can do the same for - , * and / operations 

#generate random numbers 

from numpy import random
print(random.randint(5)) # generates random numbers from 0 to 5

print(random.randint(10,size=3))

#choice random from given array

j=np.array([12,8,9,10,69])
print(random.choice(j))  # from j array random generate

#log base in numpy
print(np.log2(j)) # log2 
print(np.log10(j)) #log10

#lcm and gcd

k=6
j=7
print(np.lcm(6,7))
print(np.gcd(6,7))


















