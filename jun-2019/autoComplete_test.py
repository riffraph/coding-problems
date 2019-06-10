import autoComplete as myModule

def test_1():
    list = ['dog', 'deer', 'deal', 'a']
    tree = myModule.listToTree(list)
    result = myModule.search('de', tree)
    assert(result == ['deer', 'deal'])

test_1()


def test_2():
    list = ['bee', 'a', 'month', 'are', 'best']
    tree = myModule.listToTree(list)
    result = myModule.search('a', tree)
    assert(result == ['a', 'are'])

test_2()
