import numpy.random as ran
import matplotlib.pyplot as plt
from math import log, exp

a = 1.0
c = 1.0 / (2 * exp(-a) + 2 * a)
delta = 0.1


def reverseFunction(alpha):
    if alpha < c * exp(-a):
        return log(alpha / c)

    if alpha < c * (exp(-a) + 2 * a):
        return -a + (alpha - c * exp(-a)) / c

    return -log(exp(-a) - (alpha - c * (exp(-a) + 2 * a)) / c)


def generateDecompositionVelue():
    k = ran.uniform()

    if k < c * exp(-a):
        return -a - c * ran.exponential()

    if k < c * (exp(-a) + 2 * a):
        return ran.uniform() * 2 * a - a

    return a + c * ran.exponential()


def generateReverseValue():
    return reverseFunction(ran.uniform())


def plotByBuckets(values, name):
    buckets = dict()
    for x in values:
        if x >= 0:
            num = int(x / delta)
        else:
            num = int(x / delta) - 1

        if abs(num) > 10.0 / delta:
            continue

        if num in buckets:
            buckets[num] = buckets[num] + 1
        else:
            buckets[num] = 1

    items = sorted(buckets.items())

    plt.plot([delta * item[0] for item in items], [item[1] for item in items], label=name)
    plt.xlabel("x")
    plt.ylabel("times")
    plt.legend()
    plt.savefig(name + ".png")
    plt.close()


if __name__ == '__main__':
    reverse_values = []
    decomposition_values = []
    for i in range(1000000):
        reverse_values.append(generateReverseValue())
        decomposition_values.append(generateDecompositionVelue())
    plotByBuckets(reverse_values, "Reverse function method")
    plotByBuckets(decomposition_values, "Decomposition method")
