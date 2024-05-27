class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    # Getters y setters para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres")

    # Getters y setters para edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero no negativo")

    # Getters y setters para dni
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        if isinstance(dni, str) and dni.isdigit() and len(dni) == 8:
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de 8 dígitos numéricos")

    # Método para mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}")
        print(f"DNI: {self._dni}")

    # Método para verificar si es mayor de edad
    def es_mayor_de_edad(self):
        return self._edad >= 18

# Ejemplo de uso
persona = Persona("Marina", 58, "123655678")
persona.mostrar()
print("Es mayor de edad:", persona.es_mayor_de_edad())


# Clase cuenta
class Cuenta:

    # Inicia los atributos (titular - cantidad)
    def __init__(self, titular, cantidad=0.0):
        if not isinstance(titular, Persona):
            raise ValueError("El titular debe ser una instancia de la clase Persona")
        self._titular = titular
        self._cantidad = cantidad
    
    # Getters para titular y cantidad
    @property
    def titular(self):
        return self._titular

    @property
    def cantidad(self):
        return self._cantidad

    # Funcion mostrar (imprime los datos de la cuenta, incluyendo los datos del titular)
    def mostrar(self):
        print("Datos de la cuenta:")
        self._titular.mostrar()
        print(f"Cantidad: {self._cantidad:.2f}")

    # Funcion ingresar (suma la cantidad especifica al saldo si es positiva)
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
        else:
            print("La cantidad a ingresar debe ser positiva.")

    # Funcion retirar (resta la cantidad especifica del saldo)
    def retirar(self, cantidad):
        self._cantidad -= cantidad

# Ejemplo de uso
persona = Persona("Juan", 30, "12345678")
cuenta = Cuenta(persona, 100.0)
cuenta.mostrar()

cuenta.ingresar(50.0)
cuenta.mostrar()

cuenta.retirar(30.0)
cuenta.mostrar()

cuenta.retirar(150.0)
cuenta.mostrar()


class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    # Getters & Setters para bonificacion
    @property
    def bonificacion(self):
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        if isinstance(bonificacion, (int, float)) and bonificacion >= 0:
            self._bonificacion = bonificacion
        else:
            raise ValueError("La bonificación debe ser un número no negativo")
    
    # Funcion es_titular_valido (Verifica que el titular es mayor de edad (+= 18) y menor a 25 (-25))
    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25

    # Funcion retirar (retira dinero si el titular es valido)
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para retirar dinero.")

    # Funcion mostrar (muestra mensaje de "cuenta joven" y la bonificacion)
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificación: {self._bonificacion:.2f}%")

# Ejemplo de uso
persona = Persona("Juan", 20, "12345678")
cuenta_joven = CuentaJoven(persona, 100.0, 10.0)
cuenta_joven.mostrar()

cuenta_joven.ingresar(50.0)
cuenta_joven.mostrar()

cuenta_joven.retirar(30.0)
cuenta_joven.mostrar()

persona_no_valida = Persona("Ana", 30, "87654321")
cuenta_no_valida = CuentaJoven(persona_no_valida, 200.0, 15.0)
cuenta_no_valida.mostrar()

cuenta_no_valida.retirar(50.0)
cuenta_no_valida.mostrar()