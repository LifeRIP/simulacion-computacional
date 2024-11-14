# Importación de paquetes
import matplotlib.pyplot as plt
import random

# Creación de la función Roll Dice


def roll_dice():

    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    # Determinar si los dados son del mismo número
    if die_1 == die_2:
        same_num = True
    else:
        same_num = False
    return same_num


# Entradas
num_simulaciones = 10000
max_num_rolls = 1000
apuesta = 1

# Seguimiento de
probabilidad_de_ganar = []
balance_final = []


# Creación de figuras para saldos de simulación
fig = plt.figure()
plt.title("Juego de dados de Monte Carlo [ " + str(num_simulaciones) + " simulations]")
plt.xlabel("Número de tirada")
plt.ylabel("Saldo[$]")
plt.xlim([0, max_num_rolls])

# Bucle for que se ejecutará durante la cantidad de simulaciones deseadas
for i in range(num_simulaciones):
    balance = [1000]
    num_rolls = [0]
    num_wins = 0
    # Ejecutar hasta que el jugador haya lanzado 1000 veces
    while num_rolls[-1] < max_num_rolls:
        same = roll_dice()
        # Resultado si los dados son del mismo número
        if same:
            balance.append(balance[-1] + 4 * apuesta)
            num_wins += 1
        # Resultado si los dados son números diferentes
        else:
            balance.append(balance[-1] - apuesta)
        num_rolls.append(num_rolls[-1] + 1)
        # Almacena las variables de seguimiento y agrega una línea a la figura
    probabilidad_de_ganar.append(num_wins/num_rolls[-1])
    balance_final.append(balance[-1])
    plt.plot(num_rolls, balance)

# Mostrar el gráfico después de finalizar las simulaciones
plt.show()
# Promedio de la probabilidad de victoria y el saldo final
general_probabilidad_victoria = sum(probabilidad_de_ganar)/len(probabilidad_de_ganar)
general_balance_final = sum(balance_final)/len(balance_final)
# Visualización de los promedios
print("Probabilidad promedio de ganar después de " + str(num_simulaciones) + " ejecuciones: " + str(general_probabilidad_victoria))
print("Saldo final promedio después de " + str(num_simulaciones) + " ejecuciones: $" + str(general_balance_final))
