import numpy
import string
import matplotlib.pyplot as plt

from colorama import Fore
a = numpy.zeros([3, 2])
print(Fore.RED)
print(a)
a[0, 0] = 15
a[0, 1] = 26
a[1, 0] = 99
a[1, 1] = 67
a[2, 0] = 89
a[2, 1] = 12
print('\n')

print(a)

for c in range(1,25):
    print(Fore.GREEN)
    print(abs(c - c**c))
    print('\n')

matpyplot.imshow(a, interpolation="nearest")

