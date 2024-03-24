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

        for child, _ in current_node.children:
            if not child in visited:
                stack.append(child)



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

        for child in current_node.children:
            
            if child[0] in local_derivatives.keys() :
                local_derivatives[child[0]] += child[1]() * local_derivatives[current_node]
            else:
                local_derivatives[child[0]]  = child[1]() * local_derivatives[current_node]

    return local_derivatives
