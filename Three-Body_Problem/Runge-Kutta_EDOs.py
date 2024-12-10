import numpy as np
import matplotlib.pyplot as plt

# Código de implementação das EDOs referentes ao problema
def EDOs( x , y , u , v , mu) :
    r1 = np.sqrt ((x - mu) **2 + y **2)
    r2 = np.sqrt ((x + 1 - mu) **2 + y **2)
    fu = -(1 - mu) *(x - mu) / r1 **3 - mu*(x + 1 - mu) / r2 **3 + x + 2*v

    fv = -(1 - mu) *y / r1 **3 - mu*y / r2 **3 + y - 2*u
    return np.array ([u , v , fu , fv])

# Implementação do método de Runge-Kutta
def runge_kutta_step( x , y , u , v , mu , dt ) :
    k1 = dt * EDOs( x , y , u , v , mu)
    k2 = dt * EDOs( x + 0.5 * k1[0] , y + 0.5 * k1[1] , u + 0.5 * k1[2] , v + 0.5 * k1[3] , mu)
    k3 = dt * EDOs( x + 0.5 * k2[0] , y + 0.5 * k2[1] , u + 0.5 * k2[2] , v + 0.5 * k2[3] , mu)
    k4 = dt * EDOs( x + k3[0] , y + k3[1] , u + k3[2] , v + k3[3] , mu)

    x_new = x + ( k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0] ) / 6
    y_new = y + ( k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1] ) / 6
    u_new = u + ( k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2] ) / 6
    v_new = v + ( k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3] ) / 6
    
    return x_new , y_new , u_new , v_new

 # Condicoes inicais do problema segundo uma bibliografia referência
x = -0.60739559520
y = -0.77749682650
u = 0.10833422340
v = -0.08463997159
mu = 0.00005250000

# Incremento temporal
dt = 0.2

# Numero de passos
num_steps = 5000

# Listas para armazenar os resultados
x_vals = [x]
y_vals = [y]

# Resolvendo com o metodo de Runge− K u t t a
for _ in range (num_steps):
    x, y, u, v = runge_kutta_step(x, y, u, v, mu, dt)
    x_vals.append(x)
    y_vals.append(y)

x_vals_ua = np.array(x_vals) * 30
y_vals_ua = np.array(y_vals) * 30





