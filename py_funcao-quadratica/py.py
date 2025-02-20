import math
import numpy as np
import matplotlib.pyplot as plt

a = float(input('Digite o valor de a - diferente de 0: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

if a == 0: # Verifica se a é diferente de 0
    print('O valor de a deve ser diferente de 0')
    exit()

# Calcula o valor de delta
delta = b**2 - 4*a*c

# Calcula as raízes da equação
if delta < 0: 
    print('A equação não possui raízes reais')
    exit()
elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
elif delta == 0:
    x1 = -b / (2*a)
    x2 = x1

print("x1: ", x1)
print("x2: ", x2)

# Calcula o X do vértice
xv = -b / (2*a)
# Definindo de intervalo de valores para x
x_min = xv - 10
x_max = xv + 10

# Criando um array de valores de x entre x_min e x_max
x_arr = np.linspace(x_min, x_max, 400)
# Criando um array de valores de y correspondentes aos valores de x
y_arr = a*x_arr**2 + b*x_arr + c

# Plotando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_arr, y_arr, label="f(x) = {a}x² + {b}x + {c}", color='blue')
plt.axhline(0, color='black', linewidth=0.5) # Eixo X
plt.axvline(0, color='black', linewidth=0.5)# Eixo Y
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da função quadrática')
plt.grid(True)
plt.legend()
plt.show()