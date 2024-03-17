from ReAD import Node, derivatives, boxit

N=50
M=200
def gun(x,y):
    r=x*y
    for _ in range(N):
        r=r+x*y
    return r 

@boxit
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


x=Node(5)
y=Node(2)

def m1():
    F=fun(x,y)
    for i in range(M):
        F=F+fun(x,y)

    DF = derivatives(F)
    # print(DF[y].value)
    DDF=derivatives(DF[x])
    print(DDF[y].value)
    
    memory_use = process.memory_info().rss
    print(f"With checkpoint: {memory_use / (1024 * 1024):.2f} MB")

def m2():
    G=gun(x,y)
    for i in range(M):
        G=G+gun(x,y)

    DG = derivatives(G)
    # print(DG[y].value)
    DDG=derivatives(DG[x])
    print(DDG[y].value)

    
    memory_use = process.memory_info().rss
    print(f"No checkpoint: {memory_use / (1024 * 1024):.2f} MB")

m1()
m2()
