# Joan Jaramillo - 2159930
import numpy as np
import matplotlib.pyplot as plt

def simular_cerberus(tamano_fila, tu_posicion, iteraciones=100000):
    """
    Simula el proceso de Cerberus mordiendo personas en la fila para estimar 
    la probabilidad de ser salvado según la posición inicial.
    
    Parámetros:
        tamano_fila (int): Tamaño inicial de la fila (sin incluirte).
        tu_posicion (int): Tu posición inicial en la fila (1-indexado).
        iteraciones (int): Número de simulaciones Monte Carlo.
    
    Retorna:
        probabilidad (float): Probabilidad estimada de ser salvado.
    """
    salvado = 0

    for _ in range(iteraciones):
        # Crear la fila inicial con una longitud `tamano_fila`
        fila = list(range(1, tamano_fila + 1))
        fila.insert(tu_posicion - 1, 0)  # Insertar "tú" en la fila (marcado como 0)

        while len(fila) > 3:
            # Cerberus muerde al azar una posición entre las tres primeras
            elegido = np.random.choice(3)

            # Si el elegido es "tú", cuentas como salvado
            if fila[elegido] == 0:
                salvado += 1
                break
            
            # Reestructurar la fila: El mordido se va, y el resto avanza
            fila.pop(elegido)
            fila = fila[1:] + [fila[0]]

    # Probabilidad estimada de ser salvado
    return salvado / iteraciones

# Parámetros
tamano_fila = 10  # Tamaño de la fila sin incluirte
iteraciones = 1000  # Número de simulaciones Monte Carlo

# Simular para cada posición posible
resultados = {}
for posicion in range(1, tamano_fila + 2):  # Incluye todas las posiciones posibles
    probabilidad = simular_cerberus(tamano_fila, posicion, iteraciones)
    resultados[posicion] = probabilidad

# Determinar la mejor posición
mejor_posicion = max(resultados, key=resultados.get)
print("Probabilidades por posición:", resultados)
print(f"La mejor posición es la {mejor_posicion} con una probabilidad de {resultados[mejor_posicion]:.4f}")

# Graficar los resultados
posiciones = list(resultados.keys())
probabilidades = list(resultados.values())

plt.figure(figsize=(10, 6))
plt.bar(posiciones, probabilidades, color="skyblue", edgecolor="black")
plt.xlabel("Posición en la fila")
plt.ylabel("Probabilidad de ser salvado")
plt.title("Probabilidad de ser salvado según la posición en la fila")
plt.xticks(posiciones)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()