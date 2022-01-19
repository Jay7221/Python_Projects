#! python3
# pyplot_trial.py

from matplotlib import pyplot

pyplot.plot([1,2,34,5,566,6], [1,2,3,4,5,44])
scale = 'log'
pyplot.xscale(scale)
pyplot.yscale(scale)
pyplot.title('')
pyplot.xlabel('n')
pyplot.ylabel('run time(s)')
pyplot.show()
