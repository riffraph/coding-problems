# 14 June 2019
# Given two singly linked lists that intersect at some point, find
# the intersecting node. The lists are non-cyclical.
# Do this in O(m + n) time and constant space

import logging
import sys

def getLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    stdoutHandler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stdoutHandler)

    return logger


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def arrayToLinkedList(array):
    root = None
    for val in reversed(array):
        root = Node(val, root)

    return root


def findLinkedListIntersect(list1, list2):
    logger = getLogger()

    list1Dict = {}
    currNode = list1

    # load dictionary with list 1 values
    while not (currNode is None):
        if not(currNode.val in list1Dict):
            list1Dict[currNode.val] = currNode

        currNode = currNode.next

    # scan list 2 and look up dictionary
    currNode = list2
    while not (currNode is None):
        if currNode.val in list1Dict:
            return currNode

        currNode = currNode.next

    return None