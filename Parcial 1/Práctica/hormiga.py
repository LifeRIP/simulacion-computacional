import random
import math

# Coordenadas de la hormiga
ant = [-2, 2]

# Coordenadas grano de arroz
rice = [10, 8]

# Distancia más lejana
furthest_distance = 0

# Direccion de la hormiga
def dir_ant(coords, dir):
    if dir == 'right':
        coords[0] += random.randint(1, 3)
    elif dir == 'left':
        coords[0] -= random.randint(1, 3)
    elif dir == 'up':
        coords[1] += random.randint(1, 3)
    elif dir == 'down':
        coords[1] -= random.randint(1, 3)
    return coords

def simulate_ant(attempts):
    global ant # Se declara como global para poder modificarla
    global furthest_distance

    for i in range(attempts):
        random_dir = random.choice(['right', 'left', 'up', 'down'])
        ant = dir_ant(ant, random_dir)
        distance = math.sqrt((ant[0] - rice[0])**2 + (ant[1] - rice[1])**2)
        if distance > furthest_distance:
            furthest_distance = distance

        if ant == rice:
            print("La hormiga ha encontrado el grano de arroz en", i + 1, "pasos")
            break

    if ant != rice:
        print("La hormiga no ha encontrado el grano de arroz en", attempts, "pasos")
    print("La distancia más lejana que ha estado de la posición del grano de arroz es", furthest_distance)

simulate_ant(100)