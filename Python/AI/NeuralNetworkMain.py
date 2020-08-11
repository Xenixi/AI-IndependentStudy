import numpy as numpy
import matplotlib as matpyplot
import imageio
import glob
import ctypes


import scipy.special as scspecial
# Fixed: ##https://stackoverflow.com/questions/36394571/scipy-importerror-dll-load-failed-the-specified-module-could-not-be-found  >>> LOOK HERE. <<<
####


class neuralNetworkMain:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        print("Class")
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.lr = learningrate

        #self.wih = (numpy.random.rand(self.hnodes, self.inodes)-0.5)
        #self.who = (numpy.random.rand(self.onodes, self.hnodes) - 0.5)
        #1##1###1##
        # CHECK THIS IN THE BOOK!!!
        self.wih = numpy.random.normal(
            0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(
            0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
        #########
        self.activation_function = lambda x: scspecial.expit(x)
        pass

    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        # added 2
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # numpy.dot(self.who, hidden_outputs) ####modification 3
        final_outputs = self.activation_function(final_inputs)
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # fixed #4
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        pass

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


# mods
input_nodes = 784
hidden_nodes = 200
output_nodes = 10


learning_rate = 0.3

n = neuralNetworkMain(input_nodes, hidden_nodes, output_nodes, learning_rate)

training_data_file = open("DataSet_mnist/mnist_train.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()


scorecard = []
# Number of times for training --
epochs = 3
for e in range(epochs):
    for record in training_data_list:
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        targets = numpy.zeros(output_nodes) + 0.01
        ####look over this
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)
    pass
pass


test_data_file = open("DataSet_mnist/mnist_test.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

for record in test_data_list:
    all_values = record.split(',')
    correct_label = int(all_values[0])
   # print(correct_label, "correct label")

    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    outputs = n.query(inputs)
    label = numpy.argmax(outputs)
   # print(label, "Networks's Answer")

    if (label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)

pass
#print(scorecard)
scorecard_array = numpy.asarray(scorecard)
print("performance= ", scorecard_array.sum() / scorecard_array.size)

ins  = []
img_array = imageio.imread("CUSTOMINPUT/svn.png", as_gray = True)
img_data  = 255.0 - img_array.reshape(784)
img_data = (img_data / 255.0 * 0.99) + 0.01
ins.append(img_data)


outputsNew = n.query(ins)
label = numpy.argmax(outputsNew)
print("Answer:")
print(label)
print("-----")
ctypes.windll.user32.MessageBoxW(0, "Neural Network operation has completed.", "Operation Completed.", 0)

#out = n.query(ins)
