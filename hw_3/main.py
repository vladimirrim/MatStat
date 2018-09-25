import numpy.random as ra
import math
import matplotlib.pyplot as plt

k = [i for i in range(100)]

uniValues = []
expValues = []

LAMBDA = 1
THETA = 1


def calculateUni(k):
    meanUni = 0
    values = ra.uniform(0, THETA, 100)
    for val in values:
        meanUni += val ** k
    meanUni /= 100
    return ((k + 1) * meanUni) ** (1 / k)


def calculateExp(k):
    meanExp = 0
    values = ra.exponential(LAMBDA, 100)
    for val in values:
        meanExp += val ** k
    meanExp /= 100
    return (math.factorial(k) * meanExp) ** (1 / k)


if __name__ == '__main__':

    k = [i for i in range(1, 50)]
    uniValues = []
    expValues = []
    for i in range(1, 50):
        deviation = sum([(LAMBDA - calculateExp(i)) ** 2 for _ in range(50)])
        expValues.append((deviation / 50) ** 0.5)

    for i in range(1, 50):
        deviation = sum([(THETA - calculateUni(i)) ** 2 for _ in range(50)])
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
