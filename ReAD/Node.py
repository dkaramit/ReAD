from typing import List, Callable

# A Node is basically a point of tree
# A Node has a value and a list of children.abs
# The value is the value of the node, and the childen represent
# the nodesthat lie below this one and their derivatives.
# A node without childern is a variable, while a node with children is
# an operation.

#This is intented to be used as default value for the evaluate function.
#If you created a lambda for evaluate, you would have 
#a lot of function doing the same thing, but occupied 
#more memory space.
def trivial_return(x):
    return x

"""Node class represents a node in a tree structure.

Attributes:
  value (any): The value stored in this node. 
  children (list): The child nodes below this node.
  evaluate (callable): The function to evaluate this node. Default is trivial_return.
"""
class Node:
    def __init__(self, value: float, children: List=[],evaluate: Callable=trivial_return):
        self.value = value
        self.children = children
        self.evaluate=evaluate

    def __add__(lhs, rhs):
        return add(lhs, rhs)
    
    def __mul__(lhs, rhs):
        return mul(lhs, rhs)
    
#auxiliary variables
One=Node(1)
NegOne=Node(-1)
Zero=Node(0)

from .BinaryOps import add, mul