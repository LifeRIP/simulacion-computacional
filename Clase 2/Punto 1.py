# Joan Jaramillo, 2159930
# Ejercicio 1: 100 tiradas de una moneda
import random

caras = 0
cruces = 0

for i in range(100):
    tirada = random.choice(["cara", "cruz"])
    if tirada == "cara":
        caras += 1
    elif tirada == "cruz":
        cruces += 1

print("Han salido", caras, "caras, y", cruces, "cruces.")