class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion

    def __str__(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}"

class Estudiante(Persona):
    def __init__(self, nombre, direccion, carrera, semestre):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre

    def getCarrera(self):
        return self.carrera

    def getSemestre(self):
        return self.semestre

    def setCarrera(self, carrera):
        self.carrera = carrera

    def setSemestre(self, semestre):
        self.semestre = semestre

    def __str__(self):
        return f"Estudiante: {self.nombre}, Dirección: {self.direccion}, Carrera: {self.carrera}, Semestre: {self.semestre}"

class Profesor(Persona):
    def __init__(self, nombre, direccion, departamento, categoria):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    def getDepartamento(self):
        return self.departamento

    def getCategoria(self):
        return self.categoria

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def setCategoria(self, categoria):
        self.categoria = categoria

    def __str__(self):
        return f"Profesor: {self.nombre}, Dirección: {self.direccion}, Departamento: {self.departamento}, Categoría: {self.categoria}"

if __name__ == "__main__":
    print("--- Sistema de Gestión Universitaria ---")

    persona1 = Persona("Berena Arroyo", "Barrio 11 Octubre")
    print("\n--- Detalles de Persona ---")
    print(persona1)
    persona1.setDireccion("Avenida Siempre Viva 742")
    print(f"Nueva dirección de {persona1.getNombre()}: {persona1.getDireccion()}")

    estudiante1 = Estudiante("Santiago Romero", "Unidad Jorge Robledo", "Ingeniería de Sistemas", 5)
    print("\n--- Detalles de Estudiante ---")
    print(estudiante1)
    estudiante1.setSemestre(6)
    print(f"Nuevo semestre de {estudiante1.getNombre()}: {estudiante1.getSemestre()}")

    profesor1 = Profesor("Jairo Vasquez", "Urbanización Paraiso de Colores", "Ciencias de la Computación", "Titular")
    print("\n--- Detalles de Profesor ---")
    print(profesor1)
    profesor1.setCategoria("Asociado")
    print(f"Nueva categoría de {profesor1.getNombre()}: {profesor1.getCategoria()}")

    print("\n--- Lista de Personas en la Universidad ---")
    miembros_universidad = [persona1, estudiante1, profesor1]
    for miembro in miembros_universidad:
        print(miembro)
