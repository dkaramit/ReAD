from .Node import Node, One, NegOne, Zero
from .topological_sort import topological_sort


def compute_derivatives(node):

    local_derivatives={node:One}

    stack = {}
    topological_sort(node, stack)
    
    #traverse in reverse topological order
    order=len(stack)-1
    while order>=0:
        current_node = stack[order]
        order-=1

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
