import numpy

filename = "hai.csv"
raw_data = open(filename, 'r')
data = numpy.loadtxt(raw_data, delimiter=",")
print(data)
