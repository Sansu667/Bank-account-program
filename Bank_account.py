from os import system

# Creamos la clase de Persona
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Creamos la clase Cliente
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def imprimir_datos(self):
        return f"- Tu número de cuenta es: {self.numero_cuenta}\n- Tu balance es: {self.balance}"
    def depositar(self, monto_deposito):
        self.monto_deposito = monto_deposito
        self.balance += self.monto_deposito
        return(f"- ¡Tu depósito ha sido satisfactorio!\n- Tu depósito ha sido de {self.monto_deposito}")
    def retirar(self, monto_retiro):
        self.monto_retiro = monto_retiro
        if self.balance >= self.monto_retiro:
            self.balance -= self.monto_retiro
            return(f"- ¡Tu retiro ha sido satisfactorio!\n- Tu retiro ha sido de {self.monto_retiro}")
        else:
            return("- Retiro inválido. Balance insuficiente")
cliente1 = Cliente("Santiago", "Suarez", 4025215141, 1000)

# Creamos la función "crear_cliente" que creará un cliente
def crear_cliente(cliente):
    print(cliente.imprimir_datos())
crear_cliente(cliente1)

# Creamos la función "inicio" que iniciará el programa
def inicio():
    system("cls")
    print("\n")
    print(f"Bienvenido, {cliente1.nombre} {cliente1.apellido}")
    print("\n")

    eleccion_cuenta = "x"
    while not eleccion_cuenta.isnumeric() or int(eleccion_cuenta) not in range(1,543):
        print("Elige una opción: ")
        print("""
        [1] - Mostrar información
        [2] - Realizar depósito
        [3] - Realizar retiro
        [4] - Salir\n""")
        eleccion_cuenta = input()
        print(f"- Has seleccionado la opción {eleccion_cuenta}")
    return int(eleccion_cuenta)

# Creamos la función "volver_inicio" para que el usuario pueda volver a elegir opciones del programa
def volver_inicio():
    eleccion_regresar = "x"
    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("Presione V para volver al inicio: ")
salir_cuenta = False

# Creamos el bucle que dará funcionamiento al programa en general, donde su parámetro de finalización será que el usuario escriba 4 y cambie a True el valor de la variable "salir_cuenta"
while not salir_cuenta:
    cuenta = inicio()

    if cuenta == 1:
        print("\n")
        print(cliente1.imprimir_datos())
        print("\n")
        volver_inicio()
    elif cuenta == 2:
        print("\n")
        print(cliente1.depositar(2000))
        print("\n")
        volver_inicio()
    elif cuenta == 3:
        print("\n")
        print(cliente1.retirar(1000))
        print("\n")
        volver_inicio()
    elif cuenta == 4:
        print("\n")
        print("----- Gracias por utilizar tu cuenta de banco, hasta la próxima -----")
        salir_cuenta = True