# Se Tc é a temperatura corporal de um paciente (em graus absolutos), um termômetro é capaz de revelar essa temperatura segundo
# dT/dt = β(Tc −T)
# onde β = 10^−3/seg e t (medido em seg) é o tempo trancorrido na medição.
# Usandoo método de Euler, responda: Assumindo T(0) = 293 (temperatura ambiente), e uma temperatura febril ( Tc = 313), 
# qual o tempo mínimo (em minutos) necessário para uma aferição com 95 % de exatidão ?



b = 1e-3  # Constante b
Tc = 313  # Temperatura febril
T0 = 293  # Temperatura inicial
h = 0.01     # Tamanho do passo

# EDO
def dT_dt(T):
    return b * (Tc - T)

# Método de Euler
def euler_method(T0, h, num_steps):
    T = T0
    for _ in range(num_steps):
        T += h * dT_dt(T)
    return T



# Verificar a condição |T(t) - Tc| <= 0.05 * Tc
condition_met = False
num_steps = 0

while not condition_met:
    T_at_t = euler_method(T0, h, num_steps)
    condition_met = abs(T_at_t - Tc) <= 0.05 * Tc
    num_steps += 1

tempo = num_steps * h

print(f"O tempo mínimo necessário para aferição com 95% de exatidão é aproximadamente {tempo} segundos.")
