import hasSum as myModule

def test_all():
    assert(myModule.hasSum([10, 15, 3, 7], 17) == True) # example
    assert(myModule.hasSum([8, 15, 3, 7], 16) == False) # no matching sum
    assert(myModule.hasSum([8, 15, 3, 7, 8], 16) == True) # recurring number
    assert(myModule.hasSum([], 16) == False) # empty list
    assert(myModule.hasSum([-10, 5, -6], -16) == True) # negative sum