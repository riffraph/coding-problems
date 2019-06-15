import maxSubArray as myModule

def test_1():
    array = [10, 5, 2, 7, 8, 7]
    k = 3
    assert(myModule.getMaxValues(array, k) == [10, 7, 8, 8])

def test_2():
    array = [10, 5, 2, 7, 8]
    k = 3
    assert(myModule.getMaxValues(array, k) == [10, 7, 8])

def test_3():
    array = [10, 5, 2, 7]
    k = 3
    assert(myModule.getMaxValues(array, k) == [10, 7])

def test_4():
    array = [10, 5, 2, 7, 8, 7]
    k = 2
    assert(myModule.getMaxValues(array, k) == [10, 5, 7, 8, 8])