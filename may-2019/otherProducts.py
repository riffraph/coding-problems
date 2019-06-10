from operator import mul
from functools import reduce
import timeit


def otherProducts_sol1(list):
    result = []

    allProd = reduce(mul, list)

    for item in list:
        if item != 0:
            result.append(allProd / item)
        else:
            result.append(item)

    return result


def otherProducts_sol2(list):
    result = []
    pairs = []

    prevVal = 0
    # multiple each pair of items
    for i, val in enumerate(list):
        if i == 0:
            prevVal = val
        else:
            pairs.append(val * prevVal)
            prevVal = val

    pairs.append(list[0] * list[len(list) - 1]) # multiple the first and last numbers

    # populate result
    for i in range(len(list)):
        result.append(reduce(mul, filterPairs(pairs, i)))

    return result


def filterPairs(pairs, i):
    filteredPairs= []

    for j, val in enumerate(pairs):
        if j == i:
            continue
        elif i != 0 and j == (i - 1):
            continue
        elif i == 0 and j == len(pairs) - 1:
            continue
        elif j > i and (j - i) % 2 == 0: # if current pair is to the right of i and it should not be included
            continue
        elif j < i and (i - j) % 2 == 1:
            continue
        else:
            filteredPairs.append(val)

    return filteredPairs