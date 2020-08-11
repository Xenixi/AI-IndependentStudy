import numpy as numpy
import matplotlib.pyplot as matpyplot

a = numpy.zeros([3,2])
print(a)

a[0,0] = 15
a[0,1] = 59
a[1,0] = 9
a[1,1] = -29

matpyplot.imshow(a, interpolation="nearest")


matpyplot.show()

