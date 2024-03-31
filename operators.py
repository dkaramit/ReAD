import ReAD as rd

def m1(): 
    x = rd.Node(1.33)
    y = rd.Node(3.12)
    
    
    z=rd.exp(-rd.cos(x)**y)*rd.sin(y-x*y)/x

    print(x.value,y.value,z.value)
    Dz=rd.compute_derivatives(z)
    print(Dz[x].value,Dz[y].value)

    return

m1()
