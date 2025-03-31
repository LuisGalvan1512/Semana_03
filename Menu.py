class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def mostrar_lista(self):
        nodo_actual = self.head
        if not nodo_actual:
            print("La lista está vacía.")
            return
        while nodo_actual:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def contar_nodos(self):
        nodo_actual = self.head
        contador = 0
        while nodo_actual:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador

    def insertar_al_comienzo(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.head:
            self.head = nuevo_nodo
            return
        ultimo = self.head
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo

    def insertar_en_posicion(self, dato, posicion):
        if posicion < 0 or posicion > self.contar_nodos():
            print("Posición inválida.")
            return
        if posicion == 0:
            self.insertar_al_comienzo(dato)
            return
        nodo_actual = self.head
        contador = 0
        while nodo_actual:
            if contador == posicion - 1:
                nuevo_nodo = Nodo(dato)
                nuevo_nodo.siguiente = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_nodo
                return
            contador += 1
            nodo_actual = nodo_actual.siguiente

    def eliminar_del_comienzo(self):
        if not self.head:
            print("La lista está vacía.")
            return
        self.head = self.head.siguiente

    def eliminar_del_final(self):
        if not self.head:
            print("La lista está vacía.")
            return
        if not self.head.siguiente:
            self.head = None
            return
        penultimo = self.head
        while penultimo.siguiente and penultimo.siguiente.siguiente:
            penultimo = penultimo.siguiente
        penultimo.siguiente = None

    def eliminar_en_posicion(self, posicion):
        if posicion < 0 or posicion >= self.contar_nodos():
            print("Posición inválida.")
            return
        if posicion == 0:
            self.eliminar_del_comienzo()
            return
        nodo_actual = self.head
        contador = 0
        while nodo_actual:
            if contador == posicion - 1:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return
            contador += 1
            nodo_actual = nodo_actual.siguiente

    def buscar(self, dato):
        nodo_actual = self.head
        posicion = 0
        while nodo_actual:
            if nodo_actual.dato == dato:
                return posicion
            nodo_actual = nodo_actual.siguiente
            posicion += 1
        return -1

    def encontrar_n_esimo_desde_el_final(self, n):
        total_nodos = self.contar_nodos()
        if n <= 0 or n > total_nodos:
            print("Posición inválida.")
            return
        nodo_actual = self.head
        for _ in range(total_nodos - n):
            nodo_actual = nodo_actual.siguiente
        return nodo_actual.dato

    def limpiar_lista(self):
        self.head = None

def menu():
    lista = ListaEnlazada()

    while True:
        print("\n----- Menú -----")
        print("1. Agregar un elemento al comienzo")
        print("2. Agregar un elemento al final")
        print("3. Agregar un elemento en una posición específica")
        print("4. Eliminar un elemento del comienzo")
        print("5. Eliminar un elemento del final")
        print("6. Eliminar un elemento en una posición específica")
        print("7. Mostrar la lista")
        print("8. Contar los nodos")
        print("9. Buscar un valor en la lista")
        print("10. Encontrar el n-ésimo nodo desde el final")
        print("11. Limpiar la lista")
        print("12. Salir")

        opcion = input("Selecciona una opción (1-12): ")

        if opcion == '1':
            valor = int(input("Ingresa el valor a agregar al comienzo: "))
            lista.insertar_al_comienzo(valor)
        elif opcion == '2':
            valor = int(input("Ingresa el valor a agregar al final: "))
            lista.insertar_al_final(valor)
        elif opcion == '3':
            valor = int(input("Ingresa el valor a agregar: "))
            posicion = int(input("Ingresa la posición en la que insertar (comienza en 0): "))
            lista.insertar_en_posicion(valor, posicion)
        elif opcion == '4':
            lista.eliminar_del_comienzo()
        elif opcion == '5':
            lista.eliminar_del_final()
        elif opcion == '6':
            posicion = int(input("Ingresa la posición del nodo a eliminar: "))
            lista.eliminar_en_posicion(posicion)
        elif opcion == '7':
            lista.mostrar_lista()
        elif opcion == '8':
            print(f"Número de nodos en la lista: {lista.contar_nodos()}")
        elif opcion == '9':
            valor = int(input("Ingresa el valor a buscar: "))
            posicion = lista.buscar(valor)
            if posicion != -1:
                print(f"El valor {valor} se encuentra en la posición {posicion}.")
            else:
                print(f"El valor {valor} no se encuentra en la lista.")
        elif opcion == '10':
            n = int(input("Ingresa la posición n desde el final (1 es el último nodo): "))
            valor = lista.encontrar_n_esimo_desde_el_final(n)
            if valor:
                print(f"El valor del nodo {n}-ésimo desde el final es: {valor}")
        elif opcion == '11':
            lista.limpiar_lista()
            print("La lista ha sido limpiada.")
        elif opcion == '12':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige una opción entre 1 y 12.")

menu()
