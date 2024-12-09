import numpy as np

def regra_do_trapezio(func, a, b, n):
    h = (b - a) / n
    integral_sum = 0.5 * (func(a) + func(b))  # primeiro e último termo da soma

    for i in range(1, n):
        x_i = a + i * h
        integral_sum += func(x_i)

    integral_estimada = h * integral_sum
    return integral_estimada

def minha_funcao(x):
    return np.exp(-x**2)

# intervalo de integração
a = 0
b = 1

# número de subintervalos
n = 1000

h = 0.25

resultado = regra_do_trapezio(minha_funcao, a, b, n)
print("Estimativa da integral:", resultado)
