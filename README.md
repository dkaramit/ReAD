# ReAD

ReAD is an attempt for a reverse mode automatic differentiation module in `Python`. 

## Usage

- Create `Node` objects to represent mathematical expressions.
- Perform mathematical operations on `Node` objects.
- Compute derivatives of expressions using the `derivatives` function, including higher order derivatives.
- Use the `boxit` decorator to hide the internal structure of a function, effectively saving memory in some situations.


## Example

Here's a simple example of how to use the "ReAD" module:

```python
import ReAD as rd

x = rd.Node(5)
y = rd.Node(2)

# Perform operations on Node objects
f = rd.sin(x + y) * rd.exp(x)

# Compute derivatives
Df = rd.compute_derivatives(f)
print(Df[x].value)#df/dx
print(Df[y].value)#df/dx

# Compute second derivatives
DDf = rd.compute_derivatives(Df[x])
print(DDf[x].value)#d^2f/dx^2
print(DDf[y].value)#d^2f/dxdy

# Update the values of the input nodes and compute all others
rd.update_values(f, {x:0.2, y:0.3} )
Df=DDf={} #empty the derivative dictionaries (may need to run gc.collect())

#package a "large" function to potentially save some memory.
@rd.boxit
def new_fun(x,y):
    z=x+y*rd.sin(x*y)
    for _ in range(50):
        z=rd.sin(x*y)+(z+x*y)*y*y
    return z

    
```