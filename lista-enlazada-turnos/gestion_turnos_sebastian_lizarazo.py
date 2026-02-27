# Sistema de Gestion de Turnos - Ventanilla de Atencion al Cliente
# Usando Lista Enlazada Simple
# Sebastian Lizarazo - Algoritmos II

# Clase Nodo: cada cliente en la fila
class Nodo:
    def __init__(self, turno, nombre):
        self.turno = turno        # Numero de turno (unico)
        self.nombre = nombre      # Nombre del cliente
        self.siguiente = None     # Apunta al siguiente cliente


# Clase ListaEnlazada: la fila de clientes
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.contador_turno = 0   # Para generar turnos unicos

    # Verificar si la fila esta vacia
    def esta_vacia(self):
        if self.cabeza == None:
            return True
        else:
            return False

    # Agregar cliente al FINAL de la fila
    def agregar_cliente(self, nombre):
        self.contador_turno = self.contador_turno + 1
        nuevo = Nodo(self.contador_turno, nombre)

        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo

        print(f"Cliente '{nombre}' agregado con turno #{self.contador_turno}")

    # Eliminar cliente por NUMERO DE TURNO
    def eliminar_cliente(self, turno):
        if self.esta_vacia():
            print("La fila esta vacia.")
            return

        # Si es el primero
        if self.cabeza.turno == turno:
            nombre = self.cabeza.nombre
            self.cabeza = self.cabeza.siguiente
            print(f"Turno #{turno} ({nombre}) eliminado de la fila.")
            return

        # Buscar en el resto
        anterior = self.cabeza
        actual = self.cabeza.siguiente

        while actual != None:
            if actual.turno == turno:
                nombre = actual.nombre
                anterior.siguiente = actual.siguiente
                print(f"Turno #{turno} ({nombre}) eliminado de la fila.")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"Turno #{turno} no se encontro en la fila.")

    # Buscar cliente por NUMERO DE TURNO
    def buscar_cliente(self, turno):
        if self.esta_vacia():
            print("La fila esta vacia.")
            return

        actual = self.cabeza
        posicion = 1

        while actual != None:
            if actual.turno == turno:
                print(f"Turno #{turno} encontrado: {actual.nombre} (posicion {posicion})")
                return
            actual = actual.siguiente
            posicion = posicion + 1

        print(f"Turno #{turno} no se encuentra en la fila.")

    # Mostrar la fila completa
    def mostrar_fila(self):
        if self.esta_vacia():
            print("La fila esta vacia.")
            return

        print("\n------- FILA DE CLIENTES -------")
        actual = self.cabeza
        posicion = 1

        while actual != None:
            print(f"  {posicion}. Turno #{actual.turno} - {actual.nombre}")
            actual = actual.siguiente
            posicion = posicion + 1

        print("--------------------------------\n")


# Menu principal
def menu():
    fila = ListaEnlazada()

    while True:
        print("\n====== SISTEMA DE TURNOS ======")
        print("1. Agregar cliente a la fila")
        print("2. Eliminar cliente (por turno)")
        print("3. Buscar cliente (por turno)")
        print("4. Mostrar fila completa")
        print("5. Salir")
        print("===============================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            fila.agregar_cliente(nombre)

        elif opcion == "2":
            try:
                turno = int(input("Ingrese el numero de turno a eliminar: "))
                fila.eliminar_cliente(turno)
            except:
                print("Debe ingresar un numero valido.")

        elif opcion == "3":
            try:
                turno = int(input("Ingrese el numero de turno a buscar: "))
                fila.buscar_cliente(turno)
            except:
                print("Debe ingresar un numero valido.")

        elif opcion == "4":
            fila.mostrar_fila()

        elif opcion == "5":
            print("Gracias por usar el sistema. Hasta luego!")
            break

        else:
            print("Opcion no valida. Intente de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()
