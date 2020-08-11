
from colorama import Fore, Back, Style
import scipy
import numpy

import matplotlib.pyplot as matpyplot
data_file = open("DataSet_mnist/mnist_train.csv", 'r')
data_list = data_file.readlines()
data_file.close()

index = 15

print(str(len(data_list)))
i = 0
#for line in data_list:
 #   print(Fore.CYAN + str(i) + Fore.RED + ": " + line + "\n")
  #  i += 1

all_values = data_list[index].split(',')
image_array = numpy.asfarray(all_values[1:]).reshape((28,28))
print(all_values[0])
matpyplot.imshow(image_array, cmap='Greys', interpolation='None')
matpyplot.show()
scaled_input = (numpy.asfarray(all_values[1:]) / 255 * 0.99) + 0.01
#print(scaled_input)
