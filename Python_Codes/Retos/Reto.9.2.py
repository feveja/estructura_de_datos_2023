class ColaClientes:
    def __init__(self):
        self.cola = []

    def encolar(self, cliente):
        self.cola.append(cliente)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            return "La cola está vacía"

    def esta_vacia(self):
        return len(self.cola) == 0


# Crear una instancia de la cola de clientes
cola_clientes = ColaClientes()

# Agregar clientes a la cola
cola_clientes.encolar("Cliente 1")
cola_clientes.encolar("Cliente 2")
cola_clientes.encolar("Cliente 3")

# Atender clientes en orden de llegada
print(cola_clientes.desencolar())  # Imprime "Cliente 1"
print(cola_clientes.desencolar())  # Imprime "Cliente 2"
print(cola_clientes.desencolar())  # Imprime "Cliente 3"
print(cola_clientes.desencolar())  # Imprime "La cola está vacía"
