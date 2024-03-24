from .Node import Node, One, NegOne, Zero
from .topological_sort import topological_sort

def compute_derivatives(node):

    local_derivatives={node:One}

    stack = []
    topological_sort(node, stack)
    
    while stack:
        current_node = stack.pop()

        #####----I think that this is not needed---#####
        # if current_node not in local_derivatives:
            # local_derivatives[current_node] = One
        #####--------------------------------------#####

        for input_node in current_node.input_nodes:
            
            if input_node[0] in local_derivatives.keys() :
                local_derivatives[input_node[0]] += input_node[1]() * local_derivatives[current_node]
            else:
                local_derivatives[input_node[0]]  = input_node[1]() * local_derivatives[current_node]

    return local_derivatives
