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
        self.is_checkpoint = False

    def __add__(lhs, rhs):
        return add(lhs, rhs)
    
    def __mul__(lhs, rhs):
        return mul(lhs, rhs)
    
#auxiliary variables
One=Node(1)
NegOne=Node(-1)
fnOne=lambda: One #this is used in a lot of places. It is good to only have one
Zero=Node(0)

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



def checkpoint(func):
    def wrapper(*args):
        
        output_node = func(*args)
        local_derivatives = derivatives(output_node)
        
        der_wrt_inputs={}
        for node in args:
            if node in local_derivatives:
                der_wrt_inputs[node]=local_derivatives[node]
            else:
                der_wrt_inputs[node]=Zero

        derivatives_wrt_inputs = [ 
            [node, lambda: der_wrt_inputs[node]] for node in args 
            ]
        
        return Node(output_node.value, derivatives_wrt_inputs)
    
    return wrapper

def derivatives(node):
    local_derivatives = {}
    parent_local_derivative = One

    stack = [(node, parent_local_derivative)]

    while stack:
        current_node, current_parent_local_derivative = stack.pop()

        if current_node.is_checkpoint:
            # If the current node is a checkpoint, treat it as a primitive
            if current_node in local_derivatives:
                local_derivatives[current_node] += current_parent_local_derivative
            else:
                local_derivatives[current_node] = current_parent_local_derivative
            continue

        for child_node, grad_fn in current_node.children:
            child_local_derivative = grad_fn()*current_parent_local_derivative

            if child_node in local_derivatives:
                local_derivatives[child_node] += child_local_derivative
            else:
                local_derivatives[child_node] = child_local_derivative

            stack.append((child_node, child_local_derivative))

    return local_derivatives





def main():
    @checkpoint
    def fun(x,y):
        return x

    x=Node(5)
    y=Node(2)

    F=fun(x,y)


    DF = derivatives(F)

    # print( list(DF.keys()) )
    # print( DF[x].value )
    # print( DF[y].value )
    print( F.children[0][1]().value )



main()