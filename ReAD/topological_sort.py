def topological_sort(node,sorted_nodes):
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
