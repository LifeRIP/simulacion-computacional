# Joan Jaramillo, 2159930-3743
# 1. Escriba un programa que calcule la probabilidad de que el producto de los puntos de tres lanzamientos de los dados sea menor que 50.

import itertools

# Generar todas las combinaciones posibles de los lanzamientos de dos dados (6x6)
dados = list(itertools.product(range(1, 7), repeat=2))

# Imprimir las combinaciones posibles de lanzamientos de dos dados
print(f"Combinaciones posibles de lanzamientos de dos dados: {dados}")

# Inicializar el contador de casos favorables
casos_favorables = 0

# Recorrer todas las combinaciones posibles de tres lanzamientos de dos dados
for lanzamiento1 in dados:
    for lanzamiento2 in dados:
        for lanzamiento3 in dados:
            # Calcular el producto de los puntos de los tres lanzamientos
            producto = (lanzamiento1[0] * lanzamiento1[1]) + (lanzamiento2[0] * lanzamiento2[1]) + (lanzamiento3[0] * lanzamiento3[1])
            
            # Verificar si el producto es menor que 50
            if producto < 50:
                casos_favorables += 1

# Calcular el número total de combinaciones posibles
total_combinaciones = len(dados) ** 3

# Calcular la probabilidad
probabilidad = casos_favorables / total_combinaciones

# Convertir la probabilidad a porcentaje
probabilidad_porcentaje = probabilidad * 100

print(f"La probabilidad de que el producto de los puntos de tres lanzamientos de dos dados sea menor que 50 es: {probabilidad_porcentaje:.5f}%")