import ReAD as rd

N=50
M=100
def gun(x,y):
    r=x*y
    for _ in range(N):
        r=r+x*y
    return r 

@rd.boxit
def fun(x,y):
    r=x*y
    for _ in range(N):
        r=r+x*y
    return r 


import psutil
import os
import gc

# Get the current process
process = psutil.Process(os.getpid())

# Memory usage in bytes
memory_use = process.memory_info().rss
print(f"Memory start: {memory_use / (1024 * 1024):.2f} MB")


x=rd.Node(5)
y=rd.Node(2)

def m1():
    F=fun(x,y)
    for i in range(M):
        F=F+fun(x,y)

    memory_use = process.memory_info().rss
    print(f"With checkpoint, just function: {memory_use / (1024 * 1024):.2f} MB")

    DF = rd.compute_derivatives(F)[x]
    gc.collect()
    memory_use = process.memory_info().rss
    print(f"With checkpoint, 1st derivative: {memory_use / (1024 * 1024):.2f} MB")

    # print(DF[y].value)
    DDF = rd.compute_derivatives(DF)[y]
    gc.collect()
    print(DDF.value)
    
    memory_use = process.memory_info().rss
    print(f"With checkpoint, 2nd derivative: {memory_use / (1024 * 1024):.2f} MB")

def m2():
    G=gun(x,y)
    for i in range(M):
        G=G+gun(x,y)

    memory_use = process.memory_info().rss
    print(f"No checkpoint, just function: {memory_use / (1024 * 1024):.2f} MB")

    DG = rd.compute_derivatives(G)[x]
    memory_use = process.memory_info().rss
    print(f"No checkpoint, 1st derivative: {memory_use / (1024 * 1024):.2f} MB")
    # print(DG[y].value)
    DDG = rd.compute_derivatives(DG)[y]
    print(DDG.value)

    
    memory_use = process.memory_info().rss
    print(f"No checkpoint, 2nd derivative: {memory_use / (1024 * 1024):.2f} MB")

m1();gc.collect()
m2()
