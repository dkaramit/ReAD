import ReAD as rd


import psutil
import os
import gc
# Get the current process
process = psutil.Process(os.getpid())


def m1():   
    memory_use = process.memory_info().rss
    print(f"Memory start: {memory_use / (1024 * 1024):.2f} MB")
    
    x = rd.Node(0.1)
    y = rd.Node(0.2)

    z=x+y*rd.sin(x*y)
    for _ in range(500):
        z=rd.sin(x*y)+(z+x*y)*y*y

    dz=rd.compute_derivatives(z)
    print(dz[x].value,dz[y].value)
    dxdz=rd.compute_derivatives(dz[x])
    dydz=rd.compute_derivatives(dz[y])
    print(dxdz[x].value,dxdz[y].value)
    print(dydz[x].value,dydz[y].value)
    
    memory_use = process.memory_info().rss
    print(f"Memory end: {memory_use / (1024 * 1024):.2f} MB")


m1()