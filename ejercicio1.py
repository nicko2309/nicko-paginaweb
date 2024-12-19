class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def saludar (self):
        print(f"Bienvenido, Hola soy {self.nombre}!")
persona1 = Persona (nombre= "Nicolas", edad = "37", dni="32001273")
persona1.saludar()
