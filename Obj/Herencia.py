class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print(f"Hola soy {self.nombre} y hablo")
   
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario) -> None:
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

empleado1 = Empleado("Roberto", 45, "peruano", "programador", 1000)

print(empleado1.nombre)
print(empleado1.trabajo)
empleado1.hablar()