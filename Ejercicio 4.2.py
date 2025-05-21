##inmueble
class Inmueble:

    def __init__(self, identificador_inmobiliario, area, direccion):

        self.identificador_inmobiliario = identificador_inmobiliario
        self.area = area
        self.direccion = direccion
        self.precio_venta = 0.0

    def calcular_precio_venta(self, valor_area):

        self.precio_venta = self.area * valor_area
        return self.precio_venta

    def imprimir(self):

        print(f"Identificador inmobiliario = {self.identificador_inmobiliario}")
        print(f"Area = {self.area}")
        print(f"Dirección = {self.direccion}")
        print(f"Precio de venta = ${self.precio_venta:,.2f}")

###inmueble vivienda

class InmuebleVivienda(Inmueble):

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos):

        super().__init__(identificador_inmobiliario, area, direccion)
        self.numero_habitaciones = numero_habitaciones
        self.numero_banos = numero_banos

    def imprimir(self):

        super().imprimir()
        print(f"Número de habitaciones = {self.numero_habitaciones}")
        print(f"Número de baños = {self.numero_banos}")

## casa

class Casa(InmuebleVivienda):

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):

        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)
        self.numero_pisos = numero_pisos

    def imprimir(self):

        super().imprimir()
        print(f"Número de pisos = {self.numero_pisos}")

###apartamento

class Apartamento(InmuebleVivienda):

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos):

        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)

    def imprimir(self):

        super().imprimir()

###casa rural

class CasaRural(Casa):

    valor_area = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos,
                 numero_pisos, distancia_cabecera, altitud):

        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud

    def imprimir(self):

        super().imprimir()
        print(f"Distancia la cabecera municipal = {self.distancia_cabecera} km.")
        print(f"Altitud sobre el nivel del mar = {self.altitud} metros.")
        print()

##casa urbana

class CasaUrbana(Casa):

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):

        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)

    def imprimir(self):

        super().imprimir()
        print()

##apartamento familiar

class ApartamentoFamiliar(Apartamento):

    valor_area = 2000000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, valor_administracion):

        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos)
        self.valor_administracion = valor_administracion

    def imprimir(self):

        super().imprimir()
        print(f"Valor de la administración = ${self.valor_administracion:,.2f}")
        print()

###aparta estudio

class Apartaestudio(Apartamento):

    valor_area = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos):

        # Los apartaestudios tienen una sola habitación y un solo baño
        super().__init__(identificador_inmobiliario, area, direccion, 1, 1)

    def imprimir(self):

        super().imprimir()
        print()

##conjuntocerrado

class CasaConjuntoCerrado(CasaUrbana):

    valor_area = 2500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos,
                 numero_pisos, valor_administracion, tiene_piscina, tiene_campos_deportivos):

        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        self.valor_administracion = valor_administracion
        self.tiene_piscina = tiene_piscina
        self.tiene_campos_deportivos = tiene_campos_deportivos

    def imprimir(self):

        super().imprimir()
        print(f"Valor de la administración = {self.valor_administracion}")
        print(f"Tiene piscina? = {self.tiene_piscina}")
        print(f"Tiene campos deportivos? = {self.tiene_campos_deportivos}")
        print()

##casa independiente

class CasaIndependiente(CasaUrbana):

    valor_area = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):

        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)

    def imprimir(self):

        super().imprimir()
        print()

## local

class Local(Inmueble):

    class TipoLocal:
        INTERNO = "INTERNO"
        CALLE = "CALLE"

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local):

        super().__init__(identificador_inmobiliario, area, direccion)
        self.tipo_local = tipo_local

    def imprimir(self):

        super().imprimir()
        print(f"Tipo de local = {self.tipo_local}")

## local comercial

class LocalComercial(Local):

    valor_area = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local, centro_comercial):

        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self.centro_comercial = centro_comercial

    def imprimir(self):

        super().imprimir()
        print(f"Centro comercial = {self.centro_comercial}")
        print()

##oficina

class Oficina(Local):

    valor_area = 3500000

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local, es_gobierno):

        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self.es_gobierno = es_gobierno

    def imprimir(self):

        super().imprimir()
        print(f"Es oficina gubernamental = {self.es_gobierno}")
        print()

### prueba

class Prueba:

    @staticmethod
    def main():

        apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
        print("Datos apartamento")
        apto1.calcular_precio_venta(apto1.valor_area)
        apto1.imprimir()

        print("Datos apartamento")
        aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15", 1, 1)
        aptestudio1.calcular_precio_venta(aptestudio1.valor_area)
        aptestudio1.imprimir()

if __name__ == "__main__":
    Prueba.main()
