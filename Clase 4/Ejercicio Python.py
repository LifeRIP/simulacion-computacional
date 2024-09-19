# Joan Jaramillo, 2159930-3743
# Realizar el ejercicio con una semilla cuyo número inicial es 9731 deben aparecer 
# los 100 primeros números producto de la aplicación del metodo Von Neuman

# Se define la semilla
seed = 9731

# Se define la función que realiza el método de Von Neumann
def von_neumann(seed):
    # Se eleva al cuadrado la semilla
    sqr = seed ** 2

    # Se convierte la semilla en string
    sqr = str(sqr)

    # Se obtiene el número de dígitos del número
    sqr_digits = len(sqr)

    # Se verifica si el número es de 8 dígitos si no se añaden ceros al inicio
    if sqr_digits < 8:
        sqr = '0' * (8 - sqr_digits) + sqr

    # Se obtiene el número de 4 dígitos
    seed = sqr[2:6]

    # Se convierte la semilla y el cuadrado en entero
    seed = int(seed)
    sqr = int(sqr)

    return seed, sqr

# Se realiza el método de Von Neumann 100 veces
for i in range(100):
    output = von_neumann(seed)
    seed = output[0]
    print(f"[{i+1}] \t{output[0]} \t{output[1]}")
