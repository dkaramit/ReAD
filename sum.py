import ReAD as rd


from time import time
from sys import stderr

def timeit(fun):
    def wrapper(*args):
        t0=time()
        fun(*args)
        print(f"Time taken for {fun.__name__}:",round(time()-t0,5),'s',file=stderr)
    return wrapper

@timeit
def m1(): 
    x = rd.Node(0.14)
    y = rd.Node(0.23)
    
    z=(x+x)+((x+y)+y)+y
    #as you can see, the input nodes of z are only x and y!
    print(*[_[0] for _ in z.input_nodes])
    
    #the result should be the same as
    print(x,x,x,y,y,y)

    return

m1()
