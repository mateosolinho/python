class Contacto:
    def __init__(self, nombre, telefono, mail):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail

    def __str__(self):
        return f"\n[-] Nombre: {self.nombre} \n[-] Telefono: {self.telefono} \n[-] Mail: {self.mail}"