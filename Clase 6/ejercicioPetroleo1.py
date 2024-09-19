# Joan Jaramillo, 2159930-3743
# 1. Realice un algoritmo para simular el precio del barril de petróleo durante un mes de 30 días, 
#    suponiendo que son valores enteros que fluctúan en forma aleatoria entre $ 130 y $ 150 y se 
#    obtenga las siguientes respuestas:
#    a) El promedio del precio del petróleo.
#    b) ¿Cuál fue el día en el que estuvo más barato el barril de petróleo?

import random

from matplotlib import pyplot as plt


days = 30
price = []

def oil_price_simulation(days):
	for i in range(days):
		price.append(random.randint(130, 150))
		print("El precio del barril de petróleo el día", i+1, "es de:", price[i])

	prom = sum(price)/days
	print("1. El precio promedio del barril de petróleo en los últimos 30 días es de: ", prom)
	print("2. El precio mínimo del barril de petróleo en los últimos", days, "días es de:", min(price), "el día", price.index(min(price))+1)

oil_price_simulation(days)

def graph_price(price):
	plt.plot(range(1, days + 1), price, marker='o')
	plt.title("Precio del barril de petróleo en 30 días")
	plt.xlabel("Días")
	plt.ylabel("Precio")
	plt.grid(True)
	plt.xticks(range(1, days + 1)) # Ajusta el eje x para mostrar del 1 al 30
	plt.show()

graph_price(price)