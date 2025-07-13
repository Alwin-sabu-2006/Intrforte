import matlibplot.plot as plt
import numpy
x=numpy.array([1,22,44,5])
y=['apple','orange','pie','grape']
plt.pie(x,labels=y)
plt.show()
