# Joan Jaramillo, 2159930-3743
# Crear un conjunto con los números pares y múltiplos de 3 menores a 10.
conjunto = set()

for i in range(1, 11):
  if i % 2 == 0:
    conjunto.add(i)
  if i % 3 == 0:
    conjunto.add(i)

print(conjunto)

conjunto1 = set()
conjunto2 = set()

for i in range(1, 11):
  if i % 2 == 0:
    conjunto1.add(i)
  if i % 3 == 0:
    conjunto2.add(i)

print(conjunto1.union(conjunto2))


# Crear una lista con los números pares y múltiplos de 3 menores a 10.
lista = list()

for i in range(1, 11):
  if i % 2 == 0 or i % 3 == 0:
    lista.append(i)

print(lista)