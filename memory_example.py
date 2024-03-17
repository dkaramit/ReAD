import ReAD as rd

N=10
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

    DF = rd.compute_derivatives(F)
    # print(DF[y].value)
    DDF = rd.compute_derivatives(DF[x])
    print(DDF[y].value)
    
    memory_use = process.memory_info().rss
    print(f"With checkpoint: {memory_use / (1024 * 1024):.2f} MB")

def m2():
    G=gun(x,y)
    for i in range(M):
        G=G+gun(x,y)

    DG = rd.compute_derivatives(G)
    # print(DG[y].value)
    DDG = rd.compute_derivatives(DG[x])
    print(DDG[y].value)

    
    memory_use = process.memory_info().rss
    print(f"No checkpoint: {memory_use / (1024 * 1024):.2f} MB")

m1()
m2()
