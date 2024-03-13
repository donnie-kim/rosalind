# Mendel's First Law
def dominance(k, m, n):
    total_individuals = k + m + n

    DDDDo = (k / total_individuals) * ((k - 1) / (total_individuals - 1))
    DDDd = (k / total_individuals) * (m / (total_individuals - 1))
    DdDD = (m / total_individuals) * (k / (total_individuals - 1))
    DdDd = (m / total_individuals) * ((m - 1) / (total_individuals - 1)) * (3 / 4)
    DDdd = (k / total_individuals) * (n / (total_individuals - 1))
    ddDD = (n / total_individuals) * (k / (total_individuals - 1))
    Dddd = (m / total_individuals) * (n / (total_individuals - 1)) * (1 / 2)
    ddDd = (n / total_individuals) * (m / (total_individuals - 1)) * (1 / 2)
    dddd = (n / total_individuals) * ((n - 1) / (total_individuals - 1)) * (0)

    probability_dominant = DDDDo + DDDd + DdDD + DdDd + DDdd + ddDD + Dddd + ddDd + dddd
    return probability_dominant


file = open("rosalind_iprb.txt", "r")
nums = file.read().split()
k = int(nums[0])
m = int(nums[1])
n = int(nums[2])

print(dominance(k, m, n))
