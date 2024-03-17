# A Node is basically a point of tree
# A Node has a value and a list of children.abs
# The value is the value of the node, and the childen represent
# the nodesthat lie below this one and their derivatives.
# A node without childern is a variable, while a node with children is
# an operation.

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __add__(lhs, rhs):
        return add(lhs, rhs)
    
    def __mul__(lhs, rhs):
        return mul(lhs, rhs)
    
#auxiliary variables
One=Node(1)
NegOne=Node(-1)
Zero=Node(0)

from .BinaryOps import add, mul