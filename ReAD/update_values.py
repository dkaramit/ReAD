from .Node import Node
from .topological_sort import topological_sort
# Note: since the derivatives are defined as functions, their value
# is pulled from self every time is needed. So, you only need to update
# node.value!   
"""
Traverses through the tree and updates the values of all nodes.

Parameters:
node (Node): The root node to traverse from. 
values (dict): A dictionary mapping node names to new values.
"""

def update_values(root_node, values):
    stack = {}
    topological_sort(root_node, stack)

    
    #traverse in topological order
    order=0
    while order<len(stack):
        node = stack[order]
        order+=1

        if node.input_nodes:
            node.value = node.evaluate(*[child[0].value for child in node.input_nodes])
        else:
            node.value = values[node]

    return node.value




#Note: instead of passing values:dict, I could update the values of the input nodes
#externally, using node.value=... This can be mode memory efficient if the dict 
#becomes large.