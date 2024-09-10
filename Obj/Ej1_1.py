class Estudiante():
    def __init__(self, nombre, edad, grado) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")
    
    
nombre = input("Diga el nombre: ")
edad = input("Diga el edad: ")
grado = input("Diga el grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DTOS ESTUDINTE:  \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
      
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break