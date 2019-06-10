import treeSerializeDeserialize as myModule

def test_example_1():
    node = myModule.Node('root', myModule.Node('left', myModule.Node('left.left')), myModule.Node('right'))
    assert(myModule.deserialize(myModule.serialize(node)).left.left.val == 'left.left')