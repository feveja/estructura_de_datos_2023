class PilaLibros:
    def __init__(self):
        self.pila = []

    def apilar(self, libro):
        self.pila.append(libro)

    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            return "La pila está vacía"

    def esta_vacia(self):
        return len(self.pila) == 0


# Crear una instancia de la pila
pila_libros = PilaLibros()

# Apilar libros en la pila
pila_libros.apilar("Libro 1")
pila_libros.apilar("Libro 2")
pila_libros.apilar("Libro 3")

# Sacar libros de la pila
print(pila_libros.desapilar())  # Imprime "Libro 3"
print(pila_libros.desapilar())  # Imprime "Libro 2"
print(pila_libros.desapilar())  # Imprime "Libro 1"
print(pila_libros.desapilar())  # Imprime "La pila está vacía"