import numpy

#question 5.1
arr = numpy.arange(10, 26).reshape(4,4)
print("4x4 Array:\n", arr)

#question 5.2
print("Second row:", arr[1, :])
print("Last column:", arr[:, -1])

#question 5.3
arr[0, :] = 0
print("After replacing first row with zeros:\n", arr)
