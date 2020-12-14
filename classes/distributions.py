import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


class UniformDistribution:
    def __init__(self, low=0, high=1):
        self.low = low
        self.high = high


    def random(self, size=None):
        return np.random.uniform(self.low, self.high, size)


    def plot(self, num=100):
        x = np.linspace(self.low, self.high, num)
        plt.plot(x, stats.uniform.pdf(x, self.low, self.high))
        plt.show()

