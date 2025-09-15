import numpy


#question 1.1
arr1 = numpy.arange(5, 26)
print("1D Array:", arr1)

#question 1.2 
arr2 = numpy.random.randint(10, 51, size=(3,4))
print("2D Array:\n", arr2)

#question 2.1

print("Shape of arr1:", arr1.shape)
print("Size of arr1:", arr1.size)
print("Data type of arr1:", arr1.dtype)

#question 2.2
print("Shape of arr2:", arr2.shape)
print("Size of arr2:", arr2.size)
print("Data type of arr2:", arr2.dtype)

