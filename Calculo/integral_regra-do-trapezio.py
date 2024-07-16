import numpy as np

def trapezoidal_rule(f, a, b, n):
    """
    Aproxima a integral definida de f(x) no intervalo [a, b] usando a regra do trapézio com n subintervalos.
    
    :param f: função a ser integrada
    :param a: limite inferior da integração
    :param b: limite superior da integração
    :param n: número de subintervalos
    :return: valor aproximado da integral
    """
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Função a ser integrada
def f(x):
    return np.sin(x)

# Limites de integração
a = 0
b = np.pi

# Número de subintervalos
n = 1000

# Cálculo da integral
result = trapezoidal_rule(f, a, b, n)
print(f"O valor aproximado da integral de sin(x) de {a} a {b} é {result:.6f}")
