from scipy.stats import norm, chi2
import matplotlib.pyplot as plt

GAMMA = 0.5
maxN = 1000
variance = 1


def meanChi():
    lengths = []
    for n in range(1, maxN):
        length = 0
        for i in range(1, n):
            length += norm.rvs(0, variance) ** 2
        lengths.append(length * (1 / (chi2.ppf((1 - GAMMA) / 2, n)) - 1 / (chi2.ppf((1 + GAMMA) / 2, n))))
    return lengths


def squaredMean():
    lengths = []
    for n in range(1, maxN):
        length = 0
        for i in range(1, n):
            length += norm.rvs(0, variance)
        lengths.append(
            (length ** 2 / n) * (1 / ((norm.ppf((3 - GAMMA) / 4)) ** 2) - 1 / (norm.ppf((3 + GAMMA) / 4) ** 2)))
    return lengths


if __name__ == '__main__':
    plt.plot(range(1, maxN), meanChi())
    plt.xlabel('n')
    plt.ylabel('length')
    plt.title('Interval Length')
    plt.savefig('chi2.png')
    plt.close()

    plt.plot(range(1, maxN), squaredMean())
    plt.xlabel('n')
    plt.ylabel('length')
    plt.title('Interval Length')
    plt.savefig('squaredMean.png')
    plt.close()
