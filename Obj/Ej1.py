class Estudiante():
    def __init__(self, nombre, edad, grado) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    

pedro = Estudiante("Pedro", 23, 3)

print(pedro.nombre)
print(pedro.grado)
print(pedro.edad)