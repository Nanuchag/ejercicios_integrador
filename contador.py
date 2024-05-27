# Ejercicio 3

def contar_palabras(cadena):
    # Convertir la cadena a minúsculas para contar todas las palabras sin distinción de mayúsculas y minúsculas
    cadena = cadena.lower()
    
    # Dividir la cadena en palabras usando split
    palabras = cadena.split()
    
    # Crear un diccionario para contar la frecuencia de cada palabra
    frecuencia = {}
    
    # Iterar sobre las palabras
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

# Ejemplo de uso
cadena = "Solo tu maravillosa sonrisa ya es capaz de convertir este mundo en un lugar mejor en el que vivir."
frecuencia_palabras = contar_palabras(cadena)
print("Frecuencia de palabras:", frecuencia_palabras)

# Ejercicio 4

def palabra_mas_repetida(frecuencia):
    # Inicializar variables para la palabra más repetida y su frecuencia
    max_palabra = ""
    max_frecuencia = 0
    
    # Iterar sobre el diccionario para encontrar la palabra con mayor frecuencia
    for palabra, freq in frecuencia.items():
        if freq > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = freq
    
    # Devolver una tupla con la palabra más repetida y su frecuencia
    return (max_palabra, max_frecuencia)


palabra_frecuente = palabra_mas_repetida(frecuencia_palabras)
print("Palabra más repetida y su frecuencia:", palabra_frecuente)
