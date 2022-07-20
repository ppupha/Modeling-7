from numpy.random import gamma, normal
import random


class EvenDistribution:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def generate(self):
        return self.a + (self.b - self.a) * random.random()


class GammaDistribution:
    def __init__(self, k, theta):
        self.k = k
        self.theta = theta

    def generate(self):
        return gamma(self.k, self.theta)


class NormalDistribution:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def generate(self):
        return normal(self.mu, self.sigma)
