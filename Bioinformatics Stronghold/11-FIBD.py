# Mortal Fibonacci Rabbits
def mortal_fib_rabbits(n, m):
    pairs = [0] * n
    pairs[0] = 1
    pairs[1] = 1

    for i in range(2, n):
        if i < m:
            pairs[i] = pairs[i - 1] + pairs[i - 2]
        elif i == m or i == m + 1:
            pairs[i] = pairs[i - 1] + pairs[i - 2] - 1
        else:
            pairs[i] = pairs[i - 1] + pairs[i - 2] - pairs[i - (m + 1)]
    return pairs[-1]


print(mortal_fib_rabbits(91, 18))
