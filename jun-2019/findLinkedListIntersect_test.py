import findLinkedListIntersect as myModule

def test_1():
    list1 = myModule.arrayToLinkedList([3, 7, 8, 10])
    list2 = myModule.arrayToLinkedList([99, 1, 8, 10])
    assert(myModule.findLinkedListIntersect(list1, list2).val == 8)