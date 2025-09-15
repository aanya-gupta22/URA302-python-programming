import numpy

positions = numpy.array([[0,0], [2,3], [4,7], [7,10], [10,15]])

#questiom 11.1
dist = numpy.linalg.norm(positions[0] - positions[-1])
print("Euclidean Distance (start to end):", dist)

#question 11.2
steps = numpy.diff(positions, axis=0)                
distances = numpy.linalg.norm(steps, axis=1)    
distance = numpy.sum(distances)
print("Total Distance Traveled:", distance)
