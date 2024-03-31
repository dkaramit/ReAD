from math import cos as m_pow

from .Node import Node, One, NegOne, Zero

evaluate={}

fnOne=lambda: One


def add(lhs, rhs):
    if lhs.evaluate == evaluate[add] and rhs.evaluate != evaluate[add]:
       lhs.value += rhs.value
       lhs.input_nodes.append([rhs, fnOne])
       return lhs
        
    if rhs.evaluate == evaluate[add] and lhs.evaluate != evaluate[add]:
       rhs.value += lhs.value
       rhs.input_nodes.append([lhs, fnOne])
       return rhs

    if lhs.evaluate == evaluate[add] and rhs.evaluate == evaluate[add]:
       for _ in rhs.input_nodes:
            lhs.value += _[0].value
            lhs.input_nodes.append(_)
       return lhs
    
    return Node(lhs.value + rhs.value, [ [lhs,fnOne] , [rhs,fnOne] ],_add)
    
def _add(*a): 
    s=0
    for _ in a:
        s+=_
    return s
evaluate[add]=_add

def sub(lhs, rhs):
    return add(lhs, -rhs)




def derivative_of_div_num(num,den):
    def compute_derivative():
        return  One/den
    return compute_derivative
def derivative_of_div_den(num,den):
    def compute_derivative():
        return -num/(den*den)  
    return compute_derivative
def div(num, den):
    return Node(num.value / den.value, [ [num,derivative_of_div_num(num,den)] , [den,derivative_of_div_den(num,den)] ], 
    _div)
def _div(num, den):
    return num/den
evaluate[div]=_div


def derivative_of_pow_base(base,exp):
    def compute_derivative():
        return exp*base**(exp+NegOne)
    return compute_derivative
def derivative_of_pow_exp(base,exp):
    def compute_derivative():
        return  base**exp*log(base)
    return compute_derivative

def pow(base, exp):
    return Node(base.value**exp.value, [(base, derivative_of_pow_base(base,exp)),(exp, derivative_of_pow_exp(base,exp))], m_pow)
evaluate[pow]=m_pow
from .UnaryOps import log



def derivative_of_mul(var):
    def compute_derivative():
        return var  
    return compute_derivative

def mul(lhs, rhs):
    return Node(lhs.value * rhs.value, [ [lhs,derivative_of_mul(rhs)] , [rhs,derivative_of_mul(lhs)] ], 
    _mul)

def _mul(*a): 
    p=a[0]
    for _ in a[1:]:
        p*=_
    return p
evaluate[mul]=_mul

#not very efficient, but it is expressive :)
# def product(a,exclude):
#     p=One
#     s=False
#     for _ in a:
#         if _ != exclude:
#             p=mul(p,_)
#         #remove one one of the excluded nodes (the derivative of x*x should be x)
#         if _ == exclude:
#             if s:
#                 p=mul(p,_)
#             s=True
#     return p


# #it would be better to append the inputs to lhs or rhs if one of them is already mul
# def mul(lhs, rhs):
#     merged_nodes=[]
#     if lhs.evaluate == evaluate[mul]:
#         for _ in lhs.input_nodes:                
#             merged_nodes.append(_[0])
#     else:
#         merged_nodes.append(lhs)

#     if rhs.evaluate == evaluate[mul]:
#         for _ in rhs.input_nodes:                
#             merged_nodes.append(_[0])
#     else:
#         merged_nodes.append(rhs)
    
#     input_nodes=[]
#     for node in merged_nodes:
#         input_nodes.append([node , lambda exclude=node: product(merged_nodes,exclude) ])
        
#     return Node(lhs.value*rhs.value,
#         input_nodes,
#         _mul
#         )
    
# evaluate[mul]=_mul