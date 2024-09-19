# Joan Jaramillo, 2159930-3743
# 2.	Escriba un código para determinar en qué cuadrante se encuentra un punto ingresado por teclado.

# Definir la función cuadrante_punto
def cuadrante_punto(x, y):
    if x > 0 and y > 0:
        return "Primer cuadrante"
    elif x < 0 and y > 0:
        return "Segundo cuadrante"
    elif x < 0 and y < 0:
        return "Tercer cuadrante"
    elif x > 0 and y < 0:
        return "Cuarto cuadrante"
    else:
        return "Origen"

# Ingresar las coordenadas del punto
x = float(input("Ingrese la coordenada x del punto: "))
y = float(input("Ingrese la coordenada y del punto: "))
cuadrante = cuadrante_punto(x, y)
print(f"El punto ({x}, {y}) se encuentra en el {cuadrante}")
