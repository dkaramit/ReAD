import ReAD as rd


from time import time
from sys import stderr

def timeit(fun):
    def wrapper(*args):
        t0=time()
        fun(*args)
        print(f"Time taken for {fun.__name__}:",round(time()-t0,5),'s',file=stderr)
    return wrapper


evaluate={}

def _mul(*a): 
    p=a[0]
    for _ in a[1:]:
        p*=_
    return p

#not very efficient, but it is expressive :)
def product(a,exclude):
    p=rd.Node(1.)
    s=False
    for _ in a:
        if _ != exclude:
            p=mul(p,_)
        #remove one one of the excluded nodes (the derivative of x*x should be x)
        if _ == exclude:
            if s:
                p=mul(p,_)
            s=True
    return p

#it would be better to append the inputs to lhs or rhs if one of them is already mul
def mul(lhs, rhs):
    merged_nodes=[]
    if lhs.evaluate == evaluate[mul]:
        for _ in lhs.input_nodes:                
            merged_nodes.append(_[0])
    else:
        merged_nodes.append(lhs)

    if rhs.evaluate == evaluate[mul]:
        for _ in rhs.input_nodes:                
            merged_nodes.append(_[0])
    else:
        merged_nodes.append(rhs)
    
    input_nodes=[]
    for node in merged_nodes:
        input_nodes.append([node , lambda exclude=node: product(merged_nodes,exclude) ])
        
    return rd.Node(lhs.value*rhs.value,
        input_nodes,
        _mul
        )
    
evaluate[mul]=_mul

@timeit
def m1(): 
    x = rd.Node(0.14)
    y = rd.Node(0.23)
    
    z=x*x*y
    h=mul(x, mul( x , y) )



    print(*[_[0] for _ in z.input_nodes])

    # these two should be the same, and should have more 
    # inputs than z (z always has two!)
    print(*[_[0] for _ in h.input_nodes])
    print(x,x,y)


    Dz=rd.compute_derivatives(z)
    Dh=rd.compute_derivatives(h)
    
    print(z.value,Dz[x].value,Dz[y].value)
    print(h.value,Dh[x].value,Dh[y].value)

    rd.update_values(z, {x:1.2, y:4.3} )
    rd.update_values(h, {x:1.2, y:4.3} )

    Dz=rd.compute_derivatives(z)
    Dh=rd.compute_derivatives(h)
    
    print(z.value,Dz[x].value,Dz[y].value)
    print(h.value,Dh[x].value,Dh[y].value)




    return

m1()
