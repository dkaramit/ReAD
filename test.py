import ReAD as rd

def topo_sort(node,stack,visited):

    visited.add(node)
    for child, _ in node.children:
        if child not in visited:
            topo_sort(child, stack, visited)
    stack.append(node)
    return stack


def topological_sort(node):
    visited = set()
    stack = []
    sorted_nodes = []


    return sorted_nodes
    





_ONE=rd.Node(1)
def derivatives(node):

    local_derivatives={}

    visited = set()
    stack = []
    topo_sort(node, stack, visited)
    
    while stack:
        current_node = stack.pop()
        if current_node not in local_derivatives:
            local_derivatives[current_node] = _ONE

        for child in current_node.children:
            
            if child[0] in local_derivatives.keys() :
                local_derivatives[child[0]] += child[1]() * local_derivatives[current_node]
            else:
                local_derivatives[child[0]]  = child[1]() * local_derivatives[current_node]

    return local_derivatives



import psutil
import os
import gc
# Get the current process
process = psutil.Process(os.getpid())

# Memory usage in bytes
memory_use = process.memory_info().rss
print(f"Memory start: {memory_use / (1024 * 1024):.2f} MB")



def m1():
    x = rd.Node(0.1)
    y = rd.Node(0.2)

    z=x+y*rd.sin(x)
    for _ in range(50):
        z=rd.sin(z+x*y)

    dz=rd.compute_derivatives(z)
    print(dz[x].value,dz[y].value)
    dxdz=rd.compute_derivatives(dz[x])
    dydz=rd.compute_derivatives(dz[y])
    print(dxdz[x].value,dxdz[y].value)
    print(dydz[x].value,dydz[y].value)
    
    memory_use = process.memory_info().rss
    print(f"No topological order: {memory_use / (1024 * 1024):.2f} MB")

def m2():
    x = rd.Node(0.1)
    y = rd.Node(0.2)

    z=x+y*rd.sin(x)
    for _ in range(50):
        z=rd.sin(z+x*y)

    dz=derivatives(z)
    print(dz[x].value,dz[y].value)

    dxdz=derivatives(dz[x])
    dydz=derivatives(dz[y])
    print(dxdz[x].value,dxdz[y].value)
    print(dydz[x].value,dydz[y].value)

    memory_use = process.memory_info().rss
    print(f"With topological order: {memory_use / (1024 * 1024):.2f} MB")


m1();gc.collect()
m2()

# x=rd.Node(2)
# y=rd.Node(4)

# z=x+y*rd.sin(x)
# for _ in range(10):
#     z=rd.sin(z+x*y)

# t1=topo_sort(z)
# t2=topological_sort(z)

# print(set(  [ _[0]==_[1]   for _ in zip(t1,t2)  ]  ))