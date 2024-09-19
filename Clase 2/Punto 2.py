# Joan Jaramillo, 2159930
# Ejercicio 2: Pedro y Pablo

sum = 0
dif = 0
pedro = 0
pablo = 0

for i in range(1,7):
    #print(i)
    for j in range(1,7):
        sum = i + j
        dif = abs(i - j)
        if sum > 7:
            #print(sum)
            pedro += 1;
        if dif < 2:
            pablo += 1;


#print(pedro)
#print(pablo)
print("La suma es mayor que 7 en", pedro, "de los 36 casos posibles, por lo tanto tiene", pedro*100/36, "% de probabilidad de que gane Pedro")
print("La diferencia es menor que 2 en", pablo, "de los 36 casos posibles, por lo tanto tiene", pablo*100/36, "% de probabilidad de que gane Pablo")
print("Entonces, no es un juego equitativo. Pablo tiene mayor probabilidad de ganar que Pedro")
