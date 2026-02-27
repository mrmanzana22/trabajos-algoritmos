# Programa de Administracion de Fila - Atencion al Cliente
# Lista Enlazada Simple - Algoritmos II
# German Godoy

# Nodo que representa a cada persona en la fila
class Cliente:
    def __init__(self, num_turno, nom):
        self.num_turno = num_turno
        self.nom = nom
        self.sig = None


# Estructura de la fila usando lista enlazada
class Fila:
    def __init__(self):
        self.primero = None
        self.turno_actual = 0

    # Revisa si no hay nadie en la fila
    def sin_clientes(self):
        return self.primero == None

    # Nuevo cliente entra a la fila
    def nuevo_cliente(self, nom):
        self.turno_actual += 1
        cliente_nuevo = Cliente(self.turno_actual, nom)

        if self.sin_clientes():
            self.primero = cliente_nuevo
        else:
            temp = self.primero
            while temp.sig != None:
                temp = temp.sig
            temp.sig = cliente_nuevo

        print(">> " + nom + " entro a la fila con turno #" + str(self.turno_actual))

    # Cliente se retira de la fila
    def retirar_cliente(self, num):
        if self.sin_clientes():
            print(">> No hay clientes en la fila.")
            return

        # Verificar si es el primero
        if self.primero.num_turno == num:
            cliente_retirado = self.primero.nom
            self.primero = self.primero.sig
            print(">> Turno #" + str(num) + " (" + cliente_retirado + ") se retiro.")
            return

        # Recorrer buscando el turno
        ant = self.primero
        act = self.primero.sig

        while act != None:
            if act.num_turno == num:
                cliente_retirado = act.nom
                ant.sig = act.sig
                print(">> Turno #" + str(num) + " (" + cliente_retirado + ") se retiro.")
                return
            ant = act
            act = act.sig

        print(">> No existe el turno #" + str(num) + " en la fila.")

    # Buscar cliente por numero de turno
    def buscar_turno(self, num):
        if self.sin_clientes():
            print(">> Fila vacia, no hay nadie que buscar.")
            return

        temp = self.primero
        pos = 1

        while temp != None:
            if temp.num_turno == num:
                print(">> Turno #" + str(num) + " encontrado: " + temp.nom + " (posicion " + str(pos) + ")")
                return
            temp = temp.sig
            pos += 1

        print(">> Turno #" + str(num) + " no esta en la fila.")

    # Ver todos los clientes
    def ver_fila(self):
        if self.sin_clientes():
            print(">> No hay nadie en la fila.")
            return

        print("")
        print("========== CLIENTES EN FILA ==========")
        temp = self.primero
        num = 1

        while temp != None:
            print("   " + str(num) + ") Turno #" + str(temp.num_turno) + " -> " + temp.nom)
            temp = temp.sig
            num += 1

        print("=======================================")
        print("")


# Programa principal
def ejecutar():
    mi_fila = Fila()
    salir = False

    while not salir:
        print("")
        print("+--------- MENU PRINCIPAL ---------+")
        print("|  1. Nuevo cliente                |")
        print("|  2. Retirar cliente (por turno)  |")
        print("|  3. Buscar cliente (por turno)   |")
        print("|  4. Ver fila                     |")
        print("|  5. Salir                        |")
        print("+----------------------------------+")

        op = input("   Opcion: ")

        if op == "1":
            n = input("   Nombre: ")
            mi_fila.nuevo_cliente(n)

        elif op == "2":
            t = input("   Turno a retirar: ")
            if t.isdigit():
                mi_fila.retirar_cliente(int(t))
            else:
                print(">> Ingrese un numero valido.")

        elif op == "3":
            t = input("   Turno a buscar: ")
            if t.isdigit():
                mi_fila.buscar_turno(int(t))
            else:
                print(">> Ingrese un numero valido.")

        elif op == "4":
            mi_fila.ver_fila()

        elif op == "5":
            print(">> Programa finalizado.")
            salir = True

        else:
            print(">> Opcion incorrecta.")


# Iniciar programa
if __name__ == "__main__":
    ejecutar()
