import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import norm
import numpy as np

#Равномерное распределение

def ud_function(a, b, x):
    #return (x - a) / (b - a) if a <= x < b else 0 if x < a else 1
    if (x < a):
        return 0
    if (x > b):
        return 1
    return (x - a) / (b - a)


def ud_density(a, b, x):
    if (a <= x <= b):
        return 1 / (b - a)
    return 0


#Нормальное распределение
def norm_function(x, mu, sigma):
    return norm.cdf(x, mu, sqrt(sigma))


def norm_density(x, mu, sigma):
    return norm.pdf(x, mu, sqrt(sigma))


def draw_graphics(x, y_function, y_density, name):
    fig, axs = plt.subplots(2, figsize=(6, 7))

    fig.suptitle(name)
    axs[0].plot(x, y_function, color='red')
    axs[1].plot(x, y_density, color='blue')

    axs[0].set_xlabel('x')
    axs[0].set_ylabel('F(x)')

    axs[1].set_xlabel('x')
    axs[1].set_ylabel('f(x)')

    axs[0].grid(True)
    axs[1].grid(True)
    


def main():
    print('Равномерное распределение:')
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    print('Нормальное распределение:')
    mu = float(input("Input mu: "))
    sigma = float(input("Input sigma: "))

    
    delta = b - a
    x = np.arange(a - delta / 2, b + delta / 2, 0.001)
    y_function = [ud_function(a, b, _x) for _x in x]
    y_density = [ud_density(a, b, _x) for _x in x]
    draw_graphics(x, y_function, y_density, 'Равномерное распределение')

    x = np.arange(mu - 5 * sigma, mu + 5 * sigma, 0.001)
    y_function = norm_function(x, mu, sigma)
    y_density = norm_density(x, mu, sigma)
    draw_graphics(x, y_function, y_density, 'Нормальное распределение')

    plt.show()

if __name__ == '__main__':
    main()
