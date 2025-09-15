import numpy

# 6.1 Create 1D array (10 elements) random integers 20–40
arr = numpy.random.randint(20, 41, size=10)
print("Random Array:", arr)

# 6.2 Find elements > 30
print("Elements greater than 30:", arr[arr > 30])
