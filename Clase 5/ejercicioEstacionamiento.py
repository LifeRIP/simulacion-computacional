# Joan Manuel Jaramillo Avila, 2159930

import random
import math
import simpy

# Constantes de la simulación
SEMILLA = 30  # Semilla para el generador de números aleatorios
NUM_ESPACIOS = 2  # Número de espacios de estacionamiento disponibles
TIEMPO_APARCAMIENTO_MIN = 5  # Tiempo mínimo que un coche puede estar aparcado (en minutos)
TIEMPO_APARCAMIENTO_MAX = 30  # Tiempo máximo que un coche puede estar aparcado (en minutos)
T_LLEGADAS = 10  # Tiempo promedio entre llegadas de coches (en minutos)
TIEMPO_SIMULACION = 120  # Tiempo total de la simulación (en minutos)
TOT_LLEGADAS = 10  # Número total de llegadas de coches a simular

# Variables globales para almacenar resultados
te = 0.0 # tiempo de espera total
dt = 0.0 # duracion de aparcamiento total
fin = 0.0 # minuto en el que finaliza

# Función que simula el tiempo que un coche ocupa un espacio de estacionamiento
def aparcar(coche):
    global dt
    R = random.random()
    tiempo = TIEMPO_APARCAMIENTO_MAX - TIEMPO_APARCAMIENTO_MIN
    tiempo_aparcamiento = TIEMPO_APARCAMIENTO_MIN + (tiempo * R)
    yield env.timeout(tiempo_aparcamiento)
    print(" \o/ Aparcamiento listo para %s en %.2f minutos" % (coche, tiempo_aparcamiento))
    dt = dt + tiempo_aparcamiento

# Función que simula la llegada de un coche, su espera para aparcar y su salida del estacionamiento
def coche(env, name, estacionamiento):
    global te
    global fin
    llega = env.now
    print("---> %s llega al estacionamiento en minuto %.2f" % (name, llega))
    with estacionamiento.request() as request:
        yield request
        pasa = env.now
        espera = pasa - llega
        te = te + espera
        print("**** %s aparca en minuto %.2f habiendo esperado %.2f" % (name, pasa, espera))
        yield env.process(aparcar(name))
        deja = env.now
        print("<--- %s deja el estacionamiento en minuto %.2f" % (name, deja))
        fin = deja

# Función principal que genera las llegadas de coches de acuerdo a una distribución exponencial
def principal(env, estacionamiento):
    llegada = 0
    for i in range(TOT_LLEGADAS):
        R = random.random()
        llegada = -T_LLEGADAS * math.log(R)
        yield env.timeout(llegada)
        env.process(coche(env, 'Coche %d' % (i + 1), estacionamiento))

# Configuración del entorno de simulación y ejecución
print("\n---------------------------------------------------------------------")
print("------------------- Bienvenido Simulación Estacionamiento ------------------")
random.seed(SEMILLA)
env = simpy.Environment()
estacionamiento = simpy.Resource(env, NUM_ESPACIOS)
env.process(principal(env, estacionamiento))
env.run(until=TIEMPO_SIMULACION)

# Cálculo de indicadores de rendimiento
print("\nIndicadores obtenidos: ")
lpc = te / fin
print("\nLongitud promedio de la cola: %.2f" % lpc)
tep = te / TOT_LLEGADAS
print("Tiempo de espera promedio = %.2f" % tep)
upi = (dt / fin) / NUM_ESPACIOS
print("Uso promedio de la instalación = %.2f" % upi)
print("\n---------------------------------------------------------------------")

# Fórmulas matemáticas:
# Longitud promedio de la cola (LPC): lpc = te / fin
#   - lpc: Longitud promedio de la cola
#   - te: Tiempo de espera total
#   - fin: Minuto en el que finaliza la simulación

# Tiempo de espera promedio (TEP): tep = te / TOT_LLEGADAS
#   - tep: Tiempo de espera promedio
#   - te: Tiempo de espera total
#   - TOT_LLEGADAS: Número total de llegadas de coches

# Uso promedio de la instalación (UPI): upi = (dt / fin) / NUM_ESPACIOS
#   - upi: Uso promedio de la instalación
#   - dt: Duración total del aparcamiento
#   - fin: Minuto en el que finaliza la simulación
#   - NUM_ESPACIOS: Número de espacios de estacionamiento disponibles