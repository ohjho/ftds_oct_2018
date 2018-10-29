import numpy as np

# creating python list
python_list = [10,2,4,5,20]
# creating numpy array
nparray = np.array([10,2,4,5,20])


# numpy comparing with python list

# 1. numpy occupy less memory
import sys

python_list = list(range(100))
print(sys.getsizeof(python_list)*len(python_list))

numpy_array = np.arange(100)
print(sys.getsizeof(numpy_array)*len(numpy_array))


# 2. numpy runs computation on matrix manner, that is computationally faster
import time

size = 1000

l1 = list(range(size))
l2 = list(range(size))

a1 = np.arange(size)
a2 = np.arange(size)

# python list addition
start_time = time.time()
addition = [(x+y) for x,y in zip(l1,l2)]
print("python list addition for: ", (time.time()-start_time)*1000)

# numpy addition
start_time = time.time()
addition2 = a1+a2
print("numpy addition for: ",(time.time()-start_time)*1000)

print(len(addition),len(addition2))


# 3. numpy is convenient in matrix computation

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

print(a1,a2)
# addidtion
print(a1+a2)
# subtraction
print(a1-a2)
# multiplication
print(a1*a2)
# division
print(a1/a2)




# numpy official website
# https://docs.scipy.org/doc/numpy/user/quickstart.html
