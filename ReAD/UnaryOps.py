from math import exp as m_exp
from math import sin as m_sin
from math import cos as m_cos
from .Node import Node, One, NegOne, Zero

#Notice that I use functions to represent the local derivatives. This is to avoid creating more nodes than needed.
#This need becomes aparent in functions like exp, where without the lambda function, I would recursively create
#expOnentials without end.

def derivative_of_exp(var):
    def compute_derivative():
        return exp(var)  # This will be called later, not immediately.
    return compute_derivative
def exp(var:'Node')->'Node':
    return Node(m_exp(var.value), [(var, derivative_of_exp(var))], m_exp)


def derivative_of_sin(var):
    def compute_derivative():
        return cos(var)  
    return compute_derivative
def sin(var:'Node')->'Node':
    return Node(m_sin(var.value), [(var, derivative_of_sin(var))], m_sin)

def derivative_of_cos(var):
    def compute_derivative():
        return NegOne*sin(var)  
    return compute_derivative
def cos(var:'Node')->'Node':
    return Node(m_cos(var.value), [(var, derivative_of_cos(var))], m_cos)