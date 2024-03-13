# Rabbits and Reccurence Relations
def fib(n, k):
    if n == 1 or n == 2:
        return 1
    fib = [1, 1]

    for i in range(2, n):
        rabbits = fib[i - 1] + fib[i - 2] * k
        fib.append(rabbits)
    return fib[-1]


print(fib(36, 2))
