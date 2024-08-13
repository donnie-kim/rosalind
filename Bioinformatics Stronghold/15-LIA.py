# Independent Alleles
import math
from scipy.stats import binom


def read_data(filename):
    with open(filename, "r") as file:
        line = file.readline().strip()
        k, N = map(int, line.split())
    return k, N


def probability(k, N):
    p = 0.25  # Probability of getting Aa Bb
    total_offspring = 2**k

    # Calculate the probability of having at least N Aa Bb organisms
    prob = binom.sf(N - 1, total_offspring, p)  # sf is the survival function (1-cdf)

    return prob


k, N = read_data("rosalind_lia.txt")
result = probability(k, N)

print(result)

# print(n1, n2)
