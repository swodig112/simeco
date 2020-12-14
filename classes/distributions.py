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


class NormalDistribution:
    def __init__(self, mu=0, sigma=1):
        self.mu = mu
        self.sigma = sigma


    def random(self, size=None):
        return np.random.normal(self.mu, self.sigma, size)


    def plot(self, num=100):
        x = np.linspace(self.mu - 3 * self.sigma, self.mu + 3 * self.sigma, num)
        plt.plot(x, stats.norm.pdf(x, self.mu, self.sigma))
        plt.show()

