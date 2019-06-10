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