# Joan Manuel Jaramillo Avila -2159930
import numpy as np
import matplotlib.pyplot as plt

# Límites de integración
a = 0
b = 10
N = 1000

# Función para calcular el valor de f(x)
def f(x):
    return 10 + 6.32972 * x - 1.72728 * x**2 + 0.2017 * x**3 - 0.0096 * x**4 + 0.00017 * x**5

# Lista para almacenar todos los valores para la gráfica
plt_vals = []

# Iteramos a través de todos los valores para generar
# múltiples resultados y mostrar cuál es el más intenso
for _ in range(N):
    
    # Array de ceros de longitud N
    ar = np.zeros(N)
    
    # Iteramos sobre cada valor de ar y lo llenamos
    # con un valor aleatorio entre los límites a y b
    for i in range(len(ar)):
        ar[i] = np.random.uniform(a, b)

    # Variable para almacenar la suma de las funciones de diferentes
    # valores de x
    integral = 0.0
    
    # Iteramos y sumamos los valores de diferentes funciones
    # de x
    for i in ar:
        integral += f(i)
    
    # Obtenemos la respuesta mediante la fórmula derivada anteriormente
    ans = (b - a) / float(N) * integral
    
    # Añadimos la solución a una lista para graficar
    plt_vals.append(ans)

# Calculamos la media de las áreas
mean_area = np.mean(plt_vals)

# Graficamos la función f(x)
x = np.linspace(a, b, 1000)
y = f(x)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.fill_between(x, y, color='skyblue', alpha=0.4)
plt.title('Función f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.text(0.5, 0.5, f'Área = {mean_area:.4f}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

# Graficamos el histograma de las áreas calculadas
plt.subplot(1, 2, 2)
plt.hist(plt_vals, bins=30, ec='black')
plt.title('Distribución de las áreas calculadas')
plt.xlabel('Áreas')

plt.tight_layout()
#plt.savefig('Punto3.png')  # Guardamos la gráfica como un archivo de imagen
plt.show()