import ReAD as rd

x = rd.Node(5)
y = rd.Node(2)

# Perform operations on Node objects
f = rd.sin(x + y) * rd.cos(x)

# Compute derivatives
Df = rd.derivatives(f)
print(Df[x].value)#df/dx
print(Df[y].value)#df/dx

# Compute second derivatives
DDf = rd.derivatives(Df[x])
print(DDf[x].value)#d^2f/dx^2
print(DDf[y].value)#d^2f/dxdy