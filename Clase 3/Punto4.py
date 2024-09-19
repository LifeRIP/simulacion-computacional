# Joan Jaramillo, 2159930-3743
# Ejemplo 3 . Escriba un código para determinar por enumeración el espacio muestral del lanzamiento triple de un dado.

import itertools

# Generar todas las combinaciones posibles de los lanzamientos de un dado (1x6)
dado = set(itertools.product(range(1, 7), repeat=3))

print(f"Espacio muestral del lanzamiento triple de un dado: {dado}")