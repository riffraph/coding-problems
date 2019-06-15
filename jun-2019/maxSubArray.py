# 12 June 2019
# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k
# Do this in O(n) time and O(k) space

import logging
import sys

def getLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    stdoutHandler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stdoutHandler)

    return logger


def getMaxValues(array, k):
    logger = getLogger()

    result = []
    buffer = []
    for num in array:
        buffer.append(num)

        if len(buffer) == k:
            result.append(max(buffer))
            buffer = buffer[1:]

    return result