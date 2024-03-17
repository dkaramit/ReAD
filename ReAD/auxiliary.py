from .Node import Node
from .derivatives import derivatives

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