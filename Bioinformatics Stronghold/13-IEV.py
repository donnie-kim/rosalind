# Calculating Expected Offspring
"""
1. AA-AA p = 1.0
2. AA-Aa p = 1.0
3. AA-aa p = 1.0
4. Aa-Aa p = 0.75
5. Aa-aa p = 0.50
6. aa-aa p = 0.0
"""


def read_populations(filename):
    file = open(filename, "r")
    content = file.read().strip()
    populations = content.split()
    populations = [int(num) for num in populations]
    return populations


def expected_offspring(populations, n):
    E1 = populations[0] * 1 * n
    E2 = populations[1] * 1 * n
    E3 = populations[2] * 1 * n
    E4 = populations[3] * 0.75 * n
    E5 = populations[4] * 0.50 * n
    E6 = populations[5] * 0 * n
    total = E1 + E2 + E3 + E4 + E5 + E6
    return total


# print(read_populations("test.txt"))
populations = read_populations("rosalind_iev.txt")
print(expected_offspring(populations, 2))
