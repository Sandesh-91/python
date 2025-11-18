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


#reshaping the numpy  array 
#1.reshaping 1d array to 2d array
#2.reshaping(flattening) 3d to 1d array

arr_re=np.array([1,2,3,4,5,6])
reshape_arr=arr_re.reshape(2,3)
print(reshape_arr)

#2

reshape_arr1=reshape_arr.reshape(-1)
print("\n",reshape_arr1)

#iterating numpy array

#1d array
for a in reshape_arr1:
    print(a)

#2d array
for b in reshape_arr:
    print(b)

#3d array
for c in arr_three:
    print(c)


#joining numpy arrays
#1.using concatanate\
#2.using stack

#1

arr1=np.array([1,2,3])
arr2=np.array([3,4,5])
rearr12=np.concatenate((arr1,arr2))
rear=np.vstack((arr1,arr2)) #along columns
print("vstack ",rear)
#dstack along height
print("dstack ",np.dstack((arr1,arr2)))
print("columnstack ",np.column_stack((arr1,arr2)))


print("1d",rearr12)

#2

arr12=np.array([[1,2,3],[2,3,4]])
arr23=np.array([[1,3,5],[7,9,11]])
rearr123=np.stack((arr12,arr23))
rearr1234=np.hstack((arr12,arr23))  #along rows

print("2d",rearr123)
print("2d",rearr1234)



#array spliting

abc=np.array([])


