#! python3
# game_of_life.py

import numpy
import scipy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot

class Life(object):
    def __init__(self, n, mode = 'warp'):
        self.n = n
        self.mode = mode
        self.array = numpy.random.randint(0, 1, (n, n))
        self.weights = numpy.array([[1,1,1], [1,10,1], [1,1,1]])

    def step(self):
        con = scipy.ndimage.filters.convolve(self.array, self.weights, mode = self.mode)
        boolean = (con == 3) | (con == 12)| (con == 13)
        self.array = numpy.int8(boolean)

class LifeViewer(object):

    def __init__(self, life, cmap = matplotlib.cm.gray_r):
        self.life = life
        self.cmap = cmap

        self.fig = pyplot.figure()
        pyplot.axis([0, life.n, 0, life.n])
        pyplot.xticks([])
        pyplot.yticks([])

        self.pcolor = None
        self.update()

    def update(self):
        if self.pcolor:
            self.pcolor.remove()

        a = self.life.array
        self.pcolor = pyplot.pcolor(a, cmap = self.cmap)
        self.fig.canvas.draw()

    def animate(self, steps = 10):
        self.steps = steps
        self.fig.canvas.manager.window.after(1000, self.animate_callback)
        pyplot.show()

    def animate_callback(self):
        for i in range(self.steps):
            self.life.step()
            self.update
