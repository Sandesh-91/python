

# numpy libraries
import numpy as n

array = n.array((1, 6, 9))
print(array)


list = n.array([1, 2, 3])
print(list)
print(type(list))

tuple=n.array((1,3,4))
print(tuple)


# dimension of array
# zero dimension,one dimensional and two dimensional array

# zero
dim_var = n.array("sandesh")
dim_num = n.array(25)
print(f"hello{type(dim_num)}")
print(dim_num)
print(dim_var)
print(f"Dimension of array is {dim_var.ndim}")

# one
dim_var1 = n.array([1, 2, 3])
# array indexing
print(f"one-d array element {dim_var1[1]}")
print(f"Dimension of array is {dim_var1.ndim}")

#slicing of one-d numpy array
print(dim_var1[0:2]) # from 0 to 2 excluded
print(dim_var1[:2]) # from start to 2 excluded
print(dim_var1[0:]) # from 0 to last





# two
dim_var2 = n.array([[1, 2, 3], [2, 3, 4]])
dim_var3=n.array([[[1,3,5],[2,3,6]],[[3,4,5],[4,5,6]]])
print(dim_var3[0,1,2]) # 6

# array indexing
print(dim_var2[0, 2])
print(f"negative {dim_var2[0,-2]}")
print(f"negative {dim_var2[1,-1]}")
#dimension
print(f"Dimension of array is {dim_var2.ndim}")

# initialize numpy arrays using zeros

var = n.zeros([2, 3])
print(var)

# get the datatype of numpy array with integers

variable = n.array(["sandesh", "gaurav", "pushkey", "abcdefghi"])
print(variable.dtype)

# set the datatype of numpy array

variable = n.array(["hello", "boy"], dtype="S5")
print(variable.ndim)
print(variable.dtype)

#slicing with step
slice=n.array([25,30,35,40,45,50])
print(slice[0:6:2]) # with step 2
#slicing in 2d array
example_arr=n.array([[0,1,2,3,4,5],[1,2,3,4,5,6]])
print(example_arr[0:2,2:5])




