
# Ejercicio 5


# Metodo iterativo

def iterativo():
    while True:
        try:
            valor = int(input("Ingrese un número entero: "))
            return valor
        except ValueError:
            print("Eso no es un número entero. Inténtalo de nuevo.")

# Ejemplo de uso
numero = iterativo()
print("El número ingresado es:", numero)


# Metodo recursivo

def recursivo():
    try:
        valor = int(input("Ingrese un número entero: "))
        return valor
    except ValueError:
        print("Eso no es un número entero. Inténtalo de nuevo.")
        return recursivo()

# Ejemplo de uso
numero = recursivo()
print("El número ingresado es:", numero)
