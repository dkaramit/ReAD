from .Node import Node, One, NegOne, Zero


def topo_sort(node,sorted_nodes):
    visited = set()
    stack = []

    stack.append(node)

    while stack:
        current_node = stack.pop()

        if current_node in visited:
            sorted_nodes.append(current_node)
            continue

        visited.add(current_node)
        stack.append(current_node)

        for input_node, _ in current_node.input_nodes:
            if not input_node in visited:
                stack.append(input_node)



def compute_derivatives(node):

    local_derivatives={node:One}

    stack = []
    topo_sort(node, stack)
    
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
