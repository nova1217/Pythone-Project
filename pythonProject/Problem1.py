import numpy
import matplotlib.pyplot

# Load data
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
# Make Figure
fig = matplotlib.pyplot.figure(figsize=(5.0, 7.0))

# Create subplot in 3 rows and 1 column
axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)

axes1.set_ylevel('average')
axes1.plot(data.mean(axis-0))

axes2.set_ylevel('max')
axes2.plot(data.max(axis-0))

axes3.set_ylevel('min')
axes3.plot(data.min(axis-0))

fig.tight_layout()

matplotlib.pyplot.savefig('plot.png')

