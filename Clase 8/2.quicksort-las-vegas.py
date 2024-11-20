# Joan Jaramillo - 2159930
import random

def quicksort(arr, depth=0):
    indent = "  " * depth
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    print(f"{indent}Array: {arr}")
    print(f"{indent}Pivot elegido: {pivot} (índice {pivot_index})")
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f"{indent}Partición izquierda: {left}")
    print(f"{indent}Partición media: {middle}")
    print(f"{indent}Partición derecha: {right}")
    return quicksort(left, depth + 1) + middle + quicksort(right, depth + 1)

# Ejemplo de uso
arr = [34, 93, 19, 58, 12, 28, 95, 37, 23, 80, 57, 82, 55, 48, 21, 39, 53, 65, 30, 32, 84, 64, 44, 68, 36]
print("Array original:", arr)
sorted_arr = quicksort(arr)
print("Array ordenado:", sorted_arr)