def regra_simpson(f, a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)

    for i in range(2, n - 1, 2):
        integral += 2 * f(a + i * h)

    integral *= h / 3
    return integral

def funcao(x):
    return 2*x**5+5*x**3-3*x+1

# intervalo de integração
a = 1
b = 2

# número de subintervalos
n = 6

resultado = regra_simpson(funcao, a, b, n)
print("Estimativa da integral:", resultado)
