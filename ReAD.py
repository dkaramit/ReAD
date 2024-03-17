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
import gc

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

fnOne=lambda: One #this is used in a lot of places. It is good to only have one
def add(lhs, rhs):
    return Node(lhs.value + rhs.value, [ [lhs,fnOne] , [rhs,fnOne] ] )

def derivative_of_mul(var):
    def compute_derivative():
        return var  
    return compute_derivative
def mul(lhs, rhs):
    return Node(lhs.value * rhs.value, [ [lhs,derivative_of_mul(rhs)] , [rhs,derivative_of_mul(lhs)] ] )

#Notice that I use functions to represent the local derivatives. This is to avoid creating more nodes than needed.
#This need becomes aparent in functions like exp, where without the lambda function, I would recursively create
#expOnentials without end.

def derivative_of_exp(var):
    def compute_derivative():
        return exp(var)  # This will be called later, not immediately.
    return compute_derivative
def exp(var):
    return Node(m_exp(var.value), [(var, derivative_of_exp(var))])


def derivative_of_sin(var):
    def compute_derivative():
        return cos(var)  
    return compute_derivative
def sin(var):
    return Node(m_sin(var.value), [(var, derivative_of_sin(var))])

def derivative_of_cos(var):
    def compute_derivative():
        return NegOne*sin(var)  
    return compute_derivative
def cos(var):
    return Node(m_cos(var.value), [(var, derivative_of_cos(var))])


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
    

def derivative_of_this(local_derivative):
    def compute_derivative():
        return local_derivative
    return compute_derivative

def boxit(func):
    def wrapper(*args):
        
        func_node = func(*args)    
        local_derivatives = derivatives(func_node)
        children=[]

        for node in args:
            if node in local_derivatives.keys():
                children.append([node, derivative_of_this(local_derivatives[node])])
        return Node(func_node.value, children)
    return wrapper


N=50
M=200
def gun(x,y):
    r=x*y
    for _ in range(N):
        r=r+x*y
    return r 

@boxit
def fun(x,y):
    r=x*y
    for _ in range(N):
        r=r+x*y
    return r 


import psutil
import os

# Get the current process
process = psutil.Process(os.getpid())

# Memory usage in bytes
memory_use = process.memory_info().rss
print(f"Memory start: {memory_use / (1024 * 1024):.2f} MB")


x=Node(5)
y=Node(2)

def m1():
    F=fun(x,y)
    for i in range(M):
        F=F+fun(x,y)

    DF = derivatives(F)
    # print(DF[y].value)
    DDF=derivatives(DF[x])
    print(DDF[y].value)
    
    memory_use = process.memory_info().rss
    print(f"With checkpoint: {memory_use / (1024 * 1024):.2f} MB")

def m2():
    G=gun(x,y)
    for i in range(M):
        G=G+gun(x,y)

    DG = derivatives(G)
    # print(DG[y].value)
    DDG=derivatives(DG[x])
    print(DDG[y].value)

    
    memory_use = process.memory_info().rss
    print(f"No checkpoint: {memory_use / (1024 * 1024):.2f} MB")

m1()
m2()
