# Ejercicio 1 - 2

# Maximo común divisor
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Maximo común multiplo
def mcm(a, b):
    return abs(a * b) // mcd(a, b)

# Ejemplos de uso
print("MCD de 56 y 98:", mcd(56, 98))  # Debería imprimir 14
print("MCM de 56 y 98:", mcm(56, 98))  # Debería imprimir 392
