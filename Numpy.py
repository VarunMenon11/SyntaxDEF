import numpy as np

# ==========================================================================================================
# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and 
# manipulate them very efficiently.
# ==========================================================================================================

# ==========================================================================================================
# Numpy Array are formed using np.array() function. We pass a list or a tuple into the method.
# Deminsions of Array -> 1)0-D -> one value
#                        2)1-D -> group of 0-D
#                        3)2-D -> group of 1-D
#                        4)3-D -> group of 2-D
# arrayname.ndim method returns the dimension of the Arrayname
# When the array is created, you can define the number of dimensions by using the "ndmin" argument.
# ==========================================================================================================

# ==========================================================================================================
# Accessing Array -> You can access an Element by refering to its Index Number. Numpy starts with 0 index
#                    for 1-D, arrayname[Index]
#                    for 2-D, arrayname[row, column]
#                    for 3-D, arrayname[array, row , column]
#                    We can do Negetive Indexing to start array from the end
# ==========================================================================================================

# ==========================================================================================================
# Array Slicing -> A way to access elements of multiple index. we use colon(:).
#                  Eg) arr[start:end:step] -> start :- the starting index. if not given, then starts at 0
#                                             end :- The ending index. if not given, goes till the end.
#                                             step :- Determine the step of slicing
# ==========================================================================================================

arr = np.array(42)
print(arr)
print(arr.ndim)
print()

arr = np.array([1,2,3])
print(arr)
print(arr.ndim)
print(arr[1])
print(arr[0:2])
print()

arr = np.array([[1,2,3], [4,5,6]])
print(arr)
print(arr.ndim)
print(arr[0,0:2])
print()

arr = np.array([[[1,2,3], [4,5,6]], [[9,8,7],[6,5,4]]]) # [1,2,3][4,5,6] is one array and [9,8,7][6,5,4] is second array. [1,2,3] is first row of first array and [4,5,6] is second row of first array.
print(arr)
print(arr.ndim)
print(arr[1,0:2,2])
print()

# ==========================================================================================================
# Data Types -> a) i - integer
#               b) i - integer
#               c) b - boolean
#               d) u - unsigned integer
#               e) f - float
#               f) c - complex float
#               g) m - timedelta
#               h) M - datetime
#               i) O - object
#               j) S - string
#               k) U - unicode string
#               l) V - fixed chunk of memory for other type ( void )
#               The NumPy array object has a property called dtype that returns the data type of the array
#               The astype() function creates a copy of the array, to convert to different data type
# ==========================================================================================================


arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry', 'mango', 'watermelon'])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry', "Mango"], dtype="S")
print(arr.dtype)
newarr = arr.astype("U")
print(newarr.dtype)


# ==========================================================================================================
# Copy Vs View -> Copy is a new array with the same date as the original and any changes will not affect
#                 the original array. and vice versa.
#                 View does not store data but any changes will affect the original and vice versa.
#                 An Array has the attribute base that returns None if the array owns the data.
# ==========================================================================================================


arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()
x[0] = 6
y[3] = 10

print(x)
print(y)
print(x.base)
print(y.base)

# ==========================================================================================================
# Array Shape -> Number of elements in each dimension. In each Brackets([]) how many dimension is given.
#                Eg) array([[2,3],[4,3]]), Assume that [2,3] = a and [4,3] = b....so array[a,b].
#                    Hence we can say, the dimension is 2 and dimention of a and b is also 2.
#                    the shape is  = (2,2) where first 2 says about array[a,b] and second 2 says about
#                    number of elements in a and b.
# ==========================================================================================================


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

# ==========================================================================================================
# Iterating Array -> Interation means going through the array elements one by one.
#                    we use for loop. 
#                    Instead of using n for loops for n dimention. The function nditer() is a helping 
#                    function that iterates elements.
#                    We use op_dtypes argument to change the data type. It required a buffer space to change
#                    so we add flags = ['buffered'] as argument too
#                    The function edenumerate() is used to get the corresponding index of the element it 
#                    increments
# ==========================================================================================================


arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

for x in np.nditer(arr, flags = ['buffered'], op_dtypes = ['S']):
  print(x)

for index,x in np.ndenumerate(arr):
  print(index, x)
  

# ==========================================================================================================
# Joining Array -> Putting Contents of 2 or more same dimension array in one Array
#                  We use concatenate() fuction, along with axis (Default = 0)
#                  We pass a sequence of arrays that we want to join to the stack() method along the axis
#                  hstack() to stack along rows. vstack() to stack along columns. dstack() to stack along
#                  height.
# ==========================================================================================================

arr1 = np.array([2,3,4])
arr2 = np.array([5,6,7])
arr = np.concatenate((arr1, arr2), axis = 0)
print(arr)

arr = np.stack((arr1,arr2), axis= 1)
print(arr)

arr = np.hstack((arr1,arr2))
print(arr)


arr = np.vstack((arr1,arr2))
print(arr)

arr = np.dstack((arr1,arr2))
print(arr)

# ==========================================================================================================
# Splitting Array -> We use array_Split() for splitting arrays, we pass it the array we want to split and
#                    Number of splits.
# ==========================================================================================================

arr = np.concatenate((arr1, arr2), axis = 0)
print(arr)

new = np.array_split(arr,3)
print(new)
print(new[0])
print(new[1])
print(new[2])

arr = np.vstack((arr1,arr2))
print(arr)

new = np.array_split(arr,2,axis = 1)
print(new)
print(new[0])
print(new[1])


# ==========================================================================================================
# Searching Array -> We use where() method to find the index of the value. If the value is present in 
#                    multiple places then it sned a tuple consisting of all the index.
#                    searchsorted() performs binary search in the array. You can search multiple values
#                    at the same time....just pass [] values with comma.
# ==========================================================================================================

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

x = np.where(arr%2 == 0) #find the index of the values which are even
print(x)

# ==========================================================================================================
# Sorting Arrays -> sort() function will sort ur specified array. It can sort strings, or any data type.
# 
# ==========================================================================================================

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))


# ==========================================================================================================
# Filtering Array -> Getting some elements out of an existing array and creating a new array out of them is 
#                    called filtering. In Numpy, We filter using a boolean array.
#                    If True, Value is filtered. If Else, value isnt filtered.
# ==========================================================================================================

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# ==========================================================================================================
# Random Number -> Random means something that can not be predicted logically. Random numbers generated
#                  throuhg a generation algorithm are called pseudo random.
#                  Numpy offers the random module to work with it.
#                  Eg) x = random.randint(100) (to give int values)
#                      x = random.rand() (gives float values)
# ==========================================================================================================

# ==========================================================================================================
# Random Distribution -> A random distribution is a set of random numbers that follows a certain proablity
#                        density function.
#                        The choice() method allows you to generate a random value basded on an array of 
#                        values. it allows us to speciffy the probability for each value (between 0 and 1)
#                        The sum of all probability numbers should be 1.
# ==========================================================================================================

x = np.random.choice([3,5,7,8, 9], p=[0.1,0.2,0.2,0.5,0.0], size=(100))
print(x) #Here value 9 will never occur as its p = 0.0

# ==========================================================================================================
# Random Permutations -> Its provides a random arrangemnt of values in the array.
#                        two method use is shuffle() and permutation(). Shuffle() does changes on original 
#                        and permutation() doesnt affect the original
# ==========================================================================================================

arr = np.array[2,3,4,5]
print(np.random.permutation(arr))

# ==========================================================================================================
# Normal Distribution -> Use the random.normal() method.
#                        It has 3 parameters :- 1)loc - Mean Value
#                                               2)scale - Standard Deviation Value
#                                               3)size - Shape of the returned array
# ==========================================================================================================

# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2
x = np.random.normal(loc=1, scale=2, size=(2, 3))

print(x)


# ==========================================================================================================
# Some Advance stuff
# ==========================================================================================================

# TO take value from the txt file, and print it out here or edit it
filedata = np.genfromtxt('filename.txt', dolimiter=',')
filedata = filedata.astype('int32')
# You can also give condition to what shud be printed like here, its printing the values above 50
print(filedata[filedata < 50])

# ==========================================================================================================
# TO STUDY BINOMIAL AND POISSON DISTRIBUTION AND ALL....Go to this site link 
#                 https://www.w3schools.com/python/numpy/numpy_random_normal.asp
# ==========================================================================================================
