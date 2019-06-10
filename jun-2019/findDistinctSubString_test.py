import findDistinctSubString as myModule

def test_1():
    s = 'abcba'
    k = 2
    assert(myModule.findSubstr(s, k) == 'bcb')

def test_2():
    s = 'cgbaat'
    k = 3
    assert(myModule.findSubstr(s, k) == 'gbaa')