import numpy.random as ra
import math
import matplotlib.pyplot as plt

LAMBDA = 1
THETA = 1


def calculate_uni(k):
    mean_uni = 0
    values = ra.uniform(0, THETA, 100)
    for val in values:
        mean_uni += val ** k
    mean_uni /= 100
    return ((k + 1) * mean_uni) ** (1 / k)


def calculate_exp(k):
    mean_exp = 0
    values = ra.exponential(LAMBDA, 100)
    for val in values:
        mean_exp += val ** k
    mean_exp /= 100
    return (math.factorial(k) * mean_exp) ** (1 / k)


if __name__ == '__main__':

    k = [i for i in range(1, 50)]
    uniValues = []
    expValues = []
    for i in range(1, 50):
        deviation = sum([(LAMBDA - calculate_exp(i)) ** 2 for _ in range(50)])
        expValues.append((deviation / 50) ** 0.5)

    for i in range(1, 50):
        deviation = sum([(THETA - calculate_uni(i)) ** 2 for _ in range(50)])
        uniValues.append((deviation / 50) ** 0.5)

    plt.plot(k, uniValues)
    plt.xlabel('k')
    plt.ylabel('СКО')
    plt.title('Uniform distribution')
    plt.savefig('uni.png')
    plt.close()

    plt.plot(k, expValues)
    plt.xlabel('k')
    plt.ylabel('СКО')
    plt.title('Exponential distribution')
    plt.savefig('exp.png')
