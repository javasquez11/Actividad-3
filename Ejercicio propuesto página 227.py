class Mascota:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Color: {self.color}")

class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran.")

    def imprimir(self):
        super().imprimir()
        print(f"Peso: {self.peso} kg")
        print(f"¿Muerde?: {'Sí' if self.muerde else 'No'}")
        self.sonido()

class PerroGrande(Perro):
    def __init__(self, nombre, edad, color, peso, muerde, raza):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de perro: Grande")
        print(f"Raza: {self.raza}")

class PerroMediano(Perro):
    def __init__(self, nombre, edad, color, peso, muerde, raza):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de perro: Mediano")
        print(f"Raza: {self.raza}")

class PerroPequeño(Perro):
    def __init__(self, nombre, edad, color, peso, muerde, raza):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de perro: Pequeño")
        print(f"Raza: {self.raza}")

class Gato(Mascota):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean.")

    def imprimir(self):
        super().imprimir()
        print(f"Altura de salto: {self.altura_salto} cm")
        print(f"Longitud de salto: {self.longitud_salto} cm")
        self.sonido()

class GatoSinPelo(Gato):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto, raza):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de gato: Sin pelo")
        print(f"Raza: {self.raza}")

class GatoPeloLargo(Gato):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto, raza):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de gato: Pelo largo")
        print(f"Raza: {self.raza}")

class GatoPeloCorto(Gato):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto, raza):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de gato: Pelo corto")
        print(f"Raza: {self.raza}")

if __name__ == "__main__":
    print("--- Tienda de Mascotas ---")

    perro1 = PerroPequeño("Boby", 3, "Blanco", 5.2, False, "Caniche")
    print("\n--- Perro 1 ---")
    perro1.imprimir()

    perro2 = PerroMediano("Max", 5, "Marrón", 25.0, True, "Bulldog")
    print("\n--- Perro 2 ---")
    perro2.imprimir()

    perro3 = PerroGrande("Rex", 7, "Negro", 45.0, True, "Pastor Alemán")
    print("\n--- Perro 3 ---")
    perro3.imprimir()

    gato1 = GatoSinPelo("Cleo", 2, "Gris", 50, 120, "Esfinge")
    print("\n--- Gato 1 ---")
    gato1.imprimir()

    gato2 = GatoPeloLargo("Luna", 4, "Crema", 60, 150, "Angora")
    print("\n--- Gato 2 ---")
    gato2.imprimir()

    gato3 = GatoPeloCorto("Salem", 1, "Negro", 45, 100, "Azul Ruso")
    print("\n--- Gato 3 ---")
    gato3.imprimir()

    print("\n--- Sonidos generales ---")
    Perro.sonido()
    Gato.sonido()
