import math
def heron(s):
    x0 = 1
    x1 = (x0 + s/x0)/2
    iteracoes = 0
    while abs(x1 - x0) > 1e-6:
        x0 = x1
        x1 = (x0 + s/x0)/2
        iteracoes += 1
    return x1, iteracoes

def bissection(s):
    a = 0
    b = s
    iteracoes = 0
    while abs(a - b) > 1e-6:
        m = (a + b)/2
        if m*m > s:
            b = m
        else:
            a = m
        iteracoes += 1
    return m, iteracoes

def erro_relativo(x, y):
    return abs(x - y)/x * 100

def erro_absoluto(x, y):
    return abs(x - y)

resultado_heron = heron(2) [0]
resultado_bisseccao = bissection(2) [0]
true_sqrt = math.sqrt(2)

print(erro_absoluto(true_sqrt, resultado_heron))
