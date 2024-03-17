from .Node import Node, One, NegOne, Zero

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