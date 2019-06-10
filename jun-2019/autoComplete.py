# 5-Jun-2019
# autocomplete problem

class Node:
    def __init__(self, period=False, a=None, b=None, c=None, d=None, e=None, f=None, g=None, h=None, i=None, j=None, k=None, l=None, m=None, n=None, o=None, p=None, q=None, r=None, s=None, t=None, u=None, v=None, w=None, x=None, y=None, z=None):
        self.period = period
        self.children = {}

        if a != None:
            self.children['a'] = a
        if b != None:
            self.children['b'] = b
        if c != None:
            self.children['c'] = c
        if d != None:
            self.children['d'] = d
        if e != None:
            self.children['e'] = e
        if f != None:
            self.children['f'] = f
        if g != None:
            self.children['g'] = g
        if h != None:
            self.children['h'] = h
        if i != None:
            self.children['i'] = i
        if j != None:
            self.children['j'] = j
        if k != None:
            self.children['k'] = k
        if l != None:
            self.children['l'] = l
        if m != None:
            self.children['m'] = m
        if n != None:
            self.children['n'] = n
        if o != None:
            self.children['o'] = o
        if p != None:
            self.children['p'] = p
        if q != None:
            self.children['q'] = q
        if r != None:
            self.children['r'] = r
        if s != None:
            self.children['s'] = s
        if t != None:
            self.children['t'] = t
        if u != None:
            self.children['u'] = u
        if v != None:
            self.children['v'] = v
        if w != None:
            self.children['w'] = w
        if x != None:
            self.children['x'] = x
        if y != None:
            self.children['y'] = y
        if z != None:
            self.children['z'] = z



def search(query, tree):
    # find the subtree which the query string matches
    lastNode = tree
    for char in query:
        if char in lastNode.children:
            lastNode = lastNode.children[char]
        else:
            return []
            
    # given the last node, get all the branches from that node
    result = getAllBranches(lastNode, prevString=query)

    return result


def getAllBranches(tree, prevString=''):
    result = []

    if tree.period == True:
        result.append(prevString)

    for key, value in tree.children.items():
        result = result + getAllBranches(value, prevString + key)

    return result


def listToTree(list):
    tree = Node()

    for word in list:
        addWordToTree(word, tree)

    return tree 


def addWordToTree(word, tree):
    char = word[0]
    
    if char in tree.children:
        childTree = tree.children[char]
    else:
        childTree = Node()
        tree.children[char] = childTree

    remainder = word[1:]

    if not remainder:
        childTree.period = True
    else:
        addWordToTree(remainder, childTree) 

    return    