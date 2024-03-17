from .Node import Node, One, NegOne, Zero

fnOne=lambda: One #this is used in a lot of places. It is good to only have one
def add(lhs, rhs):
    return Node(
        lhs.value + rhs.value, [ [lhs,fnOne] , [rhs,fnOne] ],
        lambda l,r: l+r
        )

def derivative_of_mul(var):
    def compute_derivative():
        return var  
    return compute_derivative
def mul(lhs, rhs):
    return Node(lhs.value * rhs.value, [ [lhs,derivative_of_mul(rhs)] , [rhs,derivative_of_mul(lhs)] ], 
    lambda l,r: l*r)