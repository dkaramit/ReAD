from .Node import Node

# Note: since the derivatives are defined as functions, their value
# is pulled from self every time is needed. So, you only need to update
# node.value!   
"""
Traverses through the tree and updates the values of all nodes.

Parameters:
node (Node): The root node to traverse from. 
values (dict): A dictionary mapping node names to new values.
"""
#traverse throught the tree and update the values of all nodes
def update_values(node,values):
        stack=[[node,False]]
        while stack:
            node,visited=stack.pop()
            
            if not visited:
                if node.children:
                    stack.append([node,True])
                    for child in node.children:
                        stack.append([child[0],False])
                else:
                    node.value=values[node]
            if visited:
                node.value=node.evaluate(*[child[0].value for child in node.children])           
        return node.value

#Note: instead of passing values:dict, I could update the values of the input nodes
#externally, using node.value=... This can be mode memory efficient if the dict 
#becomes large.