from .Node import Node

#traverse throught the tree and update the values of all nodes
# Note: since the derivatives are defined as functions, their value
# is pulled from self every time is needed. So, you only need to update
# node.value!   
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