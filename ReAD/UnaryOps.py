from math import exp as m_exp
from math import sin as m_sin
from math import cos as m_cos
from math import log as m_log
from .Node import Node, One, NegOne, Zero
from .BinaryOps import evaluate




#Notice that I use functions to represent the local derivatives. This is to avoid creating more nodes than needed.
#This need becomes aparent in functions like exp, where without the lambda function, I would recursively create
#expOnentials without end.
def derivative_of_exp(var):
    def compute_derivative():
        return exp(var)  # This will be called later, not immediately.
    return compute_derivative
def exp(var):
    return Node(m_exp(var.value), [(var, derivative_of_exp(var))], m_exp)
evaluate[exp]=m_exp

def derivative_of_sin(var):
    def compute_derivative():
        return cos(var)  
    return compute_derivative
def sin(var):
    return Node(m_sin(var.value), [(var, derivative_of_sin(var))], m_sin)
evaluate[sin]=m_sin

def derivative_of_cos(var):
    def compute_derivative():
        return NegOne*sin(var)  
    return compute_derivative
def cos(var):
    return Node(m_cos(var.value), [(var, derivative_of_cos(var))], m_cos)
evaluate[cos]=m_cos


def derivative_of_neg(var):
    def compute_derivative():
        return NegOne  
    return compute_derivative
def neg(var):
    return Node(-var.value, [(var, derivative_of_neg(var))], _neg)
_neg = lambda x: -x
evaluate[neg]=_neg

def derivative_of_log(var):
    def compute_derivative():
        return One/var  
    return compute_derivative
def log(var):
    return Node(m_log(var.value), [(var, derivative_of_log(var))], m_log)
evaluate[log]=m_log
