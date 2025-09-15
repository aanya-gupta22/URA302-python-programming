import numpy

#question 10.1
A = numpy.array([[2, 1, 3],
              [0, 5, 6],
              [7, 8, 9]])

#question 10.2
det = numpy.linalg.det(A)   # Determinant
print("Determinant:", det)

inv = numpy.linalg.inv(A)   # Inverse
print("Inverse:\n", inv)

eigvals, eigvecs = numpy.linalg.eig(A)  # Eigenvalues & Eigenvectors
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)
