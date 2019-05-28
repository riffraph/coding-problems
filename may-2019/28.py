import base64

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

START_NODE = "-"
END_NODE = "|"
START_LEFT = ";"
START_RIGHT = ":"

def serialize(node):
    ## each node is encoded as: -<val>;<left>:<right>|

    nodeString = START_NODE + node.val

    nodeString = nodeString + START_LEFT
    if node.left != None:
        nodeString = nodeString + serialize(node.left)

    nodeString = nodeString + START_RIGHT
    if node.right != None:
        nodeString = nodeString + serialize(node.right)

    nodeString = nodeString + END_NODE

    return nodeString 


def deserialize(inputString):
    # should parse the input here ...
    # otherwise assuming the input string is valid
    node, str = deserializeHelper(inputString)

    return node


def deserializeHelper(inputString):
    if not (START_NODE in inputString):
        return None

    tmpList = inputString.split(START_NODE, 1)[1].split(START_LEFT, 1) # find the start of the node
    
    val = tmpList[0] # get the node value
    leftChild = None
    rightChild = None

    tmpStr = tmpList[1] 
    if tmpStr.find(START_RIGHT) != 0:# get the left child .. this will have the effect of deserializing the left side of the tree first
        leftChild, tmpStr = deserializeHelper(tmpStr)

    tmpStr = tmpStr.split(START_RIGHT, 1)[1]
    if tmpStr.find(END_NODE) != 0: # get the right child
        rightChild, tmpStr = deserializeHelper(tmpStr)

    return Node(val, leftChild, rightChild), tmpStr


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert(deserialize(serialize(node)).left.left.val == 'left.left')