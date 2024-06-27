class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("[+] Contacto añadido con éxito")

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                return True        

    def mostrar_contactos(self):
        if not self.contactos:
            print("[!] No hay contactos en tu agenda")
        else:
            print(f"[+] Hay {len(self.contactos)} contactos en tu agenda")
            for contacto in self.contactos:
                print(contacto)


    def buscar_contacto(self, nombre):
        if self.contactos:
            for contacto in self.contactos:
                if contacto.nombre.lower() == nombre.lower():
                    return contacto
        else:
            return False