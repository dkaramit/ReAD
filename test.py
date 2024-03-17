import ReAD as rd




x = rd.Node(5)
y = rd.Node(2)

z=x+y*rd.sin(x)
z=rd.exp(z)

dz=rd.compute_derivatives(z)
ddz=rd.compute_derivatives(dz[x])
print(z.value)
print(dz[x].value,dz[y].value)
print(ddz[x].value,ddz[y].value)

values=rd.update_values(z,{x:5,y:15})
dz=rd.compute_derivatives(z)
ddz=rd.compute_derivatives(dz[x])
print(z.value)
print(dz[x].value,dz[y].value)
print(ddz[x].value,ddz[y].value)
