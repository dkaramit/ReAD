from .Node import Node,Zero
from .compute_derivatives import compute_derivatives

#auxiliary function to be used in the input_nodes of a node.
def derivative_of_this(local_derivative):
    def compute_derivative():
        return local_derivative
    return compute_derivative

'''
The boxit decorator takes a function, calls it to compute the node, 
extracts the local derivatives, and returns a new node with input_nodes set
to the input nodes and their corresponding derivatives. This avoids saving
the details of a given expression. It saves memory in some situations and 
increases the computational, since the local derivatives are computed when
needed and not stored.
'''
def boxit(func):
    def wrapper(*args):     
        func_node = func(*args)    
        local_derivatives = compute_derivatives(func_node)
        input_nodes=[]

        for node in args:
            if node in local_derivatives.keys():
                input_nodes.append([node, derivative_of_this(local_derivatives[node])])
            else:
                input_nodes.append([node, derivative_of_this(Zero)])
        return Node(func_node.value, input_nodes)
    return wrapper