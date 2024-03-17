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
Df = rd.derivatives(f)
print(Df[x].value)#df/dx
print(Df[y].value)#df/dx

# Compute second derivatives
DDf = rd.derivatives(Df[x])
print(DDf[x].value)#d^2f/dx^2
print(DDf[y].value)#d^2f/dxdy
```