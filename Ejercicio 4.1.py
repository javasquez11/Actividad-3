### cuenta
import math

class Cuenta:
    def __init__(self, saldo, tasa_anual):
        self.saldo = saldo
        self.numero_consignaciones = 0
        self.numero_retiros = 0
        self.tasa_anual = tasa_anual
        self.comision_mensual = 0

    def consignar(self, cantidad):
        self.saldo += cantidad
        self.numero_consignaciones += 1

    def retirar(self, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo -= cantidad
            self.numero_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        tasa_mensual = self.tasa_anual / 12
        interes_mensual = self.saldo * tasa_mensual
        self.saldo += interes_mensual

    def extracto_mensual(self):
        self.saldo -= self.comision_mensual
        self.calcular_interes()

### cuenta ahorros

class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        self.activa = False
        if saldo >= 10000:
            self.activa = True

    def retirar(self, cantidad):
        if self.activa:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        if self.activa:
            super().consignar(cantidad)

    def extracto_mensual(self):
        if self.numero_retiros > 4:
            self.comision_mensual += (self.numero_retiros - 4) * 1000
        super().extracto_mensual()
        if self.saldo < 10000:
            self.activa = False
        else:
            self.activa = True # Added to reactivate if saldo goes above 10000 again

    def imprimir(self):
        print(f"Saldo = $ {self.saldo}")
        print(f"Comisión mensual = $ {self.comision_mensual}")
        print(f"Número de transacciones = {self.numero_consignaciones + self.numero_retiros}")
        print()


### cuenta corriente
class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        self.sobregiro = 0

    def retirar(self, cantidad):
        resultado = self.saldo - cantidad
        if resultado < 0:
            self.sobregiro -= resultado  # sobregiro becomes positive
            self.saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        if self.sobregiro > 0:
            residuo = cantidad - self.sobregiro # Corrected logic for depositing into overdrawn account
            if residuo >= 0:
                self.sobregiro = 0
                self.saldo = residuo
            else:
                self.sobregiro = abs(residuo) # Corrected logic for depositing into overdrawn account
                self.saldo = 0
        else:
            super().consignar(cantidad)

    def extracto_mensual(self):
        super().extracto_mensual()

    def imprimir(self):
        print(f"Saldo = $ {self.saldo}")
        print(f"Cargo mensual = $ {self.comision_mensual}")
        print(f"Número de transacciones = {self.numero_consignaciones + self.numero_retiros}")
        print(f"Valor de sobregiro = ${self.sobregiro}") # Corrected print statement
        print()


# PruebaCuenta
def main():
    print("Cuenta de ahorros")
    try:
        saldo_inicial_ahorros = float(input("Ingrese saldo inicial= $"))
        tasa_ahorros = float(input("Ingrese tasa de interés= "))
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")
        return

    cuenta1 = CuentaAhorros(saldo_inicial_ahorros, tasa_ahorros)

    try:
        cantidad_depositar = float(input("Ingresar cantidad a consignar: $"))
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")
        return
    cuenta1.consignar(cantidad_depositar)

    try:
        cantidad_retirar = float(input("Ingresar cantidad a retirar: $"))
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")
        return
    cuenta1.retirar(cantidad_retirar)

    cuenta1.extracto_mensual()
    cuenta1.imprimir()

if __name__ == "__main__":
    main()
