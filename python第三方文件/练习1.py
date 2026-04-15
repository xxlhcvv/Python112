def sum(x):
    total = 0
    for num in x:
        total += num
    return total


def mean(x):
    return sum(x) / len(x)


def sums(x):
    avg = mean(x)
    total = 0
    for num in x:
        total += (num - avg) ** 2
    return total


def var(x):
    return sums(x) / len(x)


print(var([1, 2, 3, 4, 5]))
