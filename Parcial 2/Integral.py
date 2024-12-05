# Límites de integración
a = 0
b = 10
N = 1000

# Función para calcular el valor de f(x)
def f(x):
    return 10 + 6.32972 * x - 1.72728 * x**2 + 0.2017 * x**3 - 0.0096 * x**4 + 0.00017 * x**5

# Método del trapecio
def trapezoidal_rule(a, b, N):
    h = (b - a) / N
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, N):
        integral += f(a + i * h)
    integral *= h
    return integral

resultado = trapezoidal_rule(a, b, N)
print(f"El resultado de la integral es: {resultado}")