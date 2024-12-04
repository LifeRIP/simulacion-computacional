# https://blog.espol.edu.ec/ccpg1001/3eva_it2016_t2-sensar-cultivos-con-dron/

import random
import numpy as np

def sensarCultivos(posicion):
    return 1

# Recibe dimesiones de una matriz [M, N] y retorna la 
# misma llena con valores aleatorios
def generarPlantaciones(dimension):
    return np.random.randint(1, 11, size=(dimension[0], dimension[1]))

# Plantación generada
plantacion = generarPlantaciones([2, 2])
print(plantacion)

def analizaDensidad(plantacion, limite=4):
    resultado = []

    # Recorrer matriz y rellenando otra con 'ALTO' y 'BAJO'
    for i in range(len(plantacion)):
        fila = []
        for j in range(len(plantacion[i])):
            if plantacion[i][j] < limite:
                fila.append('BAJO')
            else:
                fila.append('ALTO')
        resultado.append(fila)
    return resultado

densidad = analizaDensidad(plantacion)
print(densidad)

def reporteCrecimento(plantacion, densidad):
    resultado = []
    promedios = []
    maximos = []
    crecimiento = []
    contAltos = 0
    contBajos = 0
    altos = 0
    bajos = 0
    # Recorrer la matriz
    for i in range(len(plantacion)):
        prom = 0
        maximo = 0
        for j in range(len(plantacion[i])):
             # Sumar surcos para promediar
            prom += plantacion[i][j]

            # Sacar posicion del maximo de un surco
            maximo = maxPosition(plantacion[i])

            # Sumar y contar ALTOs y BAJOs para promediar
            if (densidad[i][j] == 'ALTO'):
                contAltos += 1
                altos += plantacion[i][j]
            else:
                contBajos +=1
                bajos += plantacion[i][j]
        
        # Agregar promedios al arreglo de promedios
        promedios.append(float(prom / len(plantacion[i])))

        # Agregar maximo al arreglo de maximos
        maximos.append(int(maximo))

    # Agregar promedios ALTO y BAJO al arreglo de crecimiento
    if (contAltos == 0):
        crecimiento.append(0)
    else:
        crecimiento.append(float(altos/contAltos))
    if (contBajos == 0):
        crecimiento.append(0)
    else:
        crecimiento.append(float(bajos/contBajos))

    # Agregar los datos al arreglo resultado
    resultado.append(promedios)
    resultado.append(maximos)
    resultado.append(crecimiento)

    return resultado

def maxPosition(arr):
    out = arr[0]
    pos = 0
    if (len(arr) == 1):
        return pos
    for i in range(len(arr) - 1):
        if (arr[i+1] > out):
            out = arr[i+1]
            pos = i+1
    return pos

print(reporteCrecimento(plantacion, densidad))