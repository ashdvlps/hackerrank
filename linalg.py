import numpy
a = []
for i in range(0, int(input())):
    a.append([float(x) for x in input().split()])

print(round(numpy.linalg.det(a),2))
