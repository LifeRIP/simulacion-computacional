# Joan Jaramillo - 2159930
import numpy as np
import matplotlib.pyplot as plt

# Definir las dimensiones del rectángulo y la función de la curva
a = 0   # coordenada x inicial del rectángulo (mínimo de x)
b = 2   # coordenada x final del rectángulo (máximo de x)
d = 1   # altura del rectángulo en el eje y
n = 10000  # número de puntos a generar

# Función de la curva y = x * e^(-x/2)
def f(x):
    return x * np.exp(-x / 2)

# Generar n puntos aleatorios dentro del rectángulo
x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, d, n)

# Contar cuántos puntos están debajo de la curva
under_curve = y_random < f(x_random)
count_under_curve = np.sum(under_curve)

# Calcular el área bajo la curva
area_rectangle = (b - a) * d
area_under_curve = (count_under_curve / n) * area_rectangle

# Imprimir el resultado
print(f"Puntos bajo la curva en el intervalo [{a}, {b}]")
print(f"Cantidad de puntos bajo la curva: {count_under_curve}")
print(f"Área aproximada bajo la curva: {area_under_curve}")

# Graficar
x_vals = np.linspace(a, b, 500)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="y = x * e^(-x/2)", color="blue")
plt.fill_between(x_vals, y_vals, color="lightblue", alpha=0.3)

# Dibujar los puntos generados
plt.scatter(x_random, y_random, color="red", s=1, label="Puntos aleatorios")
plt.scatter(x_random[under_curve], y_random[under_curve], color="green", s=1, label="Puntos bajo la curva")

# Personalizar el gráfico
plt.xlim(a, b)
plt.ylim(0, d)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title(f"Puntos bajo la curva en el intervalo [{a}, {b}] \n Cantidad de puntos bajo la curva: {count_under_curve} \n Área aproximada bajo la curva: {area_under_curve}")

plt.show()
