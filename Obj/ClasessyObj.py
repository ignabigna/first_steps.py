class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    def llamar(self):
        print(f"Estas haciendo un llamado desde: {self.modelo}")
    def cortar(self):
        print(f"Cortaste un llamado desde: {self.modelo}")
        
        
celular1 = Celular("Samsung", "S23", "48mp")
celular2 = Celular("Appel", "I15", "50mp")


print(celular2.llamar())
print(celular1.cortar())

celular1.cortar()