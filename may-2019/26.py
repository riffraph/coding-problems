def hasSum(list, k):
    diffMap = {}

    for item in list:
        # look up the current number in the diffMap
        if item in diffMap:
            return True
        else:
            # add (k - current number) to the diffMap
            diffMap[k - item] = True
        

    return False


assert(hasSum([10, 15, 3, 7], 17) == True) # example
assert(hasSum([8, 15, 3, 7], 16) == False) # no matching sum
assert(hasSum([8, 15, 3, 7, 8], 16) == True) # recurring number
assert(hasSum([], 16) == False) # empty list
assert(hasSum([-10, 5, -6], -16) == True) # negative sum