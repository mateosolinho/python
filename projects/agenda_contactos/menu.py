from agenda import Agenda
from contacto import Contacto

class Menu:
    def __init__(self, agenda):
        self.agenda = agenda

    def mostrar_menu(self):
        print("\n--- Agenda de Contactos ---")
        print("1. Añadir Contacto")
        print("2. Eliminar Contacto")
        print("3. Buscar Contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")

    def ejecutar_menu(self):
        while True:
            self.mostrar_menu()
            opcion = int(input("\n[+] Selecciona una opción: "))
            match opcion:
                case 1:
                    self.agregar_contacto()
                case 2:
                    self.eliminar_contacto()
                case 3:
                    self.buscar_contacto()
                case 4:
                    agenda.mostrar_contactos()
                case 5:
                    print("[*] Saliendo de la agenda")
                    break
                case _:
                    print("[!] Error, escoge una opción correcta")
    

    def agregar_contacto(self):
        nombre = input("\n[?] Nombre del contacto: ")
        telefono = input("[?] Telfono del contacto: ")
        email = input("[?] Email del contacto: ")
        contacto = Contacto(nombre, telefono, email)
        agenda.agregar_contacto(contacto)

    def buscar_contacto(self):
        nombre = input("\n[?] Introduce el nombre del contacto: ")
        contacto = agenda.buscar_contacto(nombre)
        if not contacto:
            print(f"\n[!] No se ha encontrado ningún contacto con el nombre {nombre}")
        else:
            print(contacto)

    def eliminar_contacto(self):
        nombre = input("\n[?] Introduce el nombre del contacto a eliminar: ")
        contacto = agenda.eliminar_contacto(nombre)
        if contacto:
            print(f"\n[+] Contacto eliminado con éxito")
        else:
            print(f"\n[!] No se ha encontrado ningún contacto con el nombre: {nombre}") # Error aquí, nunca entra
    
if __name__ == "__main__":
    agenda = Agenda()
    menu = Menu(agenda)
    menu.ejecutar_menu()