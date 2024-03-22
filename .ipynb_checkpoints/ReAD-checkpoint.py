#A basic example of Reverse mode Automatic Differentiation.

# A Node is basically a point of tree
# A Node has a value and a list of children.abs
# The value is the value of the node, and the childen represent
# the nodesthat lie below this one and their derivatives.
# A node without childern is a variable, while a node with children is
# an operation.
from math import exp as m_exp
from math import sin as m_sin
from math import cos as m_cos

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
fnOne=lambda: One #this is used in a lot of places. It is good to only have one

def add(lhs, rhs):
    return Node(lhs.value + rhs.value, [ [lhs,fnOne] , [rhs,fnOne] ] )

def mul(lhs, rhs):
    return Node(lhs.value * rhs.value, [ [lhs,lambda: rhs] , [rhs,lambda: lhs] ] )

#Notice that I use functions to represent the local derivatives. This is to avoid creating more nodes than needed.
#This need becomes aparent in functions like exp, where without the lambda function, I would recursively create
#expOnentials without end.
def exp(var):
    return Node(m_exp(var.value), [ [var, lambda: exp(var)]   ] )
def sin(var):
    return Node(m_sin(var.value), [ [var, lambda: cos(var)]   ] )
def cos(var):
    return Node(m_cos(var.value), [ [var, lambda: NegOne*sin(var)]   ] )


# def traverse_backward(node, derivatives={}, parent_local_derivative=One):
#     for child in node.children:

#         child_local_derivative = child[1]()*parent_local_derivative   
        
#         if child[0] in derivatives.keys() :
#             derivatives[child[0]] += child_local_derivative
#         else:
#             derivatives[child[0]]  = child_local_derivative
        
#         traverse_backward(child[0], derivatives, child_local_derivative)

# def derivatives(node):
#     derivatives={}
#     traverse_backward(node, derivatives)
#     return derivatives


########  with topological ordering ########
# def derivatives(node):

#     local_derivatives={}

#     def topo_sort(node, visited, stack):
#         visited.add(node)
#         for child, _ in node.children:
#             if child not in visited:
#                 topo_sort(child, visited, stack)
#         stack.append(node)

#     visited = set()
#     stack = []
#     topo_sort(node, visited, stack)

#     while stack:
#         current_node = stack.pop()
#         if current_node not in local_derivatives:
#             local_derivatives[current_node] = One

#         for child in current_node.children:
#             if child[0] in local_derivatives.keys() :
#                 local_derivatives[child[0]] += child[1]() * local_derivatives[current_node]
#             else:
#                 local_derivatives[child[0]]  = child[1]() * local_derivatives[current_node]


#     return local_derivatives


### iteratively to avoid recursion limits ###
def derivatives(node):
    local_derivatives={}
    parent_local_derivative=One

    stack = [(node, parent_local_derivative)]

    while stack:
        current_node, current_parent_local_derivative = stack.pop()

        for child_node in current_node.children:
            
            child_local_derivative = child_node[1]() * current_parent_local_derivative

            if child_node[0] in local_derivatives:
                local_derivatives[child_node[0]] += child_local_derivative
            else:
                local_derivatives[child_node[0]] = child_local_derivative

            stack.append((child_node[0], child_local_derivative))

    return local_derivatives


from time import time
from sys import stderr

def main():
    a = Node(1.)
    b = Node(1.)

    _=time()
    T=a
    
    for i in range(9999):
        T*=a 

    for i in range(10000):
        T*=b

    print(round(time()-_,3),file=stderr)

    _=time()
    derivatives1=derivatives(T)
    print(round(time()-_,3),file=stderr)

    print(derivatives1[a].value)
    print(derivatives1[b].value)



main()