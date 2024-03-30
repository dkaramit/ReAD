# def topological_sort(node,stack,visited):
    
#     visited.add(node)
#     for input_node, _ in node.input_nodes:
#         if not input_node in visited:
#             topological_sort(input_node, stack, visited)
#     stack.append(node)
#     return stack

def topological_sort(node,sorted_nodes):
    visited = set()
    stack = [node]

    while stack:
        current_node = stack.pop()
        #if the element is already in the sorted list, go to the next one
        if current_node in sorted_nodes:
            continue

        #if the element is already marked as visited, add it to the sorted list.
        #Note that the current_node is added to the list, only after its 
        # input nodes have been added to the sorted list.
        if current_node in visited:
            sorted_nodes.append(current_node)
            continue

        visited.add(current_node)
        stack.append(current_node)

        # once yo add the current node to the stack (and marked it as visited)
        # add its input nodes to the stack so that they are processed before
        # the current node. This way, the nodes that needed for the current node
        # are already in the sorted list first. Resulting in a topological 
        # ordering of the graph.
        for input_node, _ in current_node.input_nodes:
            if not input_node in visited:
                stack.append(input_node)