# Plotando graficamente a órbita de Plutão
x_netuno , y_netuno = 30 , 0
plt.figure(figsize = (10, 10), frameon = False)
plt.scatter(0, 0, s=400, label = 'Sol' , color = 'orange')
plt.scatter(x_netuno, y_netuno, s=200, label = 'Netuno', color = 'red')
plt.plot(x_vals_ua, y_vals_ua)
plt.xlim(-60 ,60)
plt.ylim(-60 ,60)
plt.title('Orbita de Plutao (Runge-Kutta)')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable = 'box')
plt.legend()
plt.show()
