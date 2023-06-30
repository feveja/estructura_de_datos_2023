class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabecera = None
        self.cola = None

    def agregar_final(self, fruta):
        nuevo_nodo = Nodo(fruta)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def agregar_inicio(self, fruta):
        nuevo_nodo = Nodo(fruta)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabecera
            self.cabecera = nuevo_nodo

    def eliminar(self, fruta):
        nodo_actual = self.cabecera
        nodo_anterior = None
        while nodo_actual:
            if nodo_actual.dato == fruta:
                if nodo_actual == self.cabecera:
                    self.cabecera = nodo_actual.siguiente
                    if nodo_actual == self.cola:
                        self.cola = None
                elif nodo_actual == self.cola:
                    self.cola = nodo_anterior
                    self.cola.siguiente = None
                else:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

    def imprimir(self):
        nodo_actual = self.cabecera
        while nodo_actual:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

    def obtener_cabecera(self):
        return self.cabecera.dato if self.cabecera else None

    def obtener_cola(self):
        return self.cola.dato if self.cola else None

# Crear una lista enlazada
lista = ListaEnlazada()

# Menú
while True:
    print("\nMENU:")
    print("A) Agregar una fruta al final de la lista")
    print("B) Agregar una fruta al inicio")
    print("C) Eliminar una fruta")
    print("D) Imprimir la lista actual")
    print("E) Obtener cabecera")
    print("F) Obtener cola")
    print("Q) Salir")

    opcion = input("Ingrese una opción: ").upper()

    if opcion == "A":
        fruta = input("Ingrese el nombre de la fruta: ")
        lista.agregar_final(fruta)
        print("Fruta agregada al final de la lista.")
    elif opcion == "B":
        fruta = input("Ingrese el nombre de la fruta: ")
        lista.agregar_inicio(fruta)
        print("Fruta agregada al inicio de la lista.")
    elif opcion == "C":
        fruta = input("Ingrese el nombre de la fruta a eliminar: ")
        lista.eliminar(fruta)
        print("Fruta eliminada de la lista.")
    elif opcion == "D":
        print("Lista actual:")
        lista.imprimir()
    elif opcion == "E":
        cabecera = lista.obtener_cabecera()
        if cabecera:
            print("Cabecera: ", cabecera)
        else:
            print("La lista está vacía.")
    elif opcion == "F":
        cola = lista.obtener_cola()
        if cola:
            print("Cola: ", cola)
        else:
            print("La lista está vacía.")
    elif opcion == "Q":
        break
    else:
        print("Opción inválida. Por favor, intente nuevamente.")
