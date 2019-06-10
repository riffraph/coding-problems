import firstMissingPositiveNumber as myModule

def test_example_1():
    inList1 = [3, 4, -1, 1]
    
    assert(myModule.findFirstMissingPositiveNumber(inList1) == 2)


def test_example_2():
    inList2 = [3, 4, -1, 1, 2]

    assert(myModule.findFirstMissingPositiveNumber(inList2) == 5)