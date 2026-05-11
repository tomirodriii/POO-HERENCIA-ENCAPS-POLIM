# Ejercicio 3: Sistema de Cuentas Bancarias
#   Crea un sistema para gestionar cuentas bancarias: CuentaCorriente y CuentaAhorros.
#    Cuenta: Clase base con atributos encapsulados (titular, saldo) y métodos para
#       depositar() y retirar().
#    CuentaCorriente: Hereda de Cuenta y permite sobregiros hasta un límite.
#    CuentaAhorros: Hereda de Cuenta y aplica un interés mensual al saldo.
#    Usa polimorfismo para implementar el método retirar() según el tipo de cuenta.

import os
os.system("cls")

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= monto

class CuentaCorriente(Cuenta):
    def __init__(self, titular, saldo, limite_sobregiro):
        super().__init__(titular, saldo)
        self.limite_sobregiro = limite_sobregiro
    
    def retirar(self, monto):
        if monto > self.saldo + self.limite_sobregiro:
            print("Fondos insuficientes, sobregiro excedido")
        else:
            self.saldo -= monto
            
class CuentaAhorros(Cuenta):
    def __init__(self, titular, saldo, tasa_interes):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes
        
    def aplicar_interes(self):
        self.saldo += self.saldo * self.tasa_interes / 100

# Ejemplo

if __name__ == "__main__":
    cuenta_corriente = CuentaCorriente("Laura Martínez", 1000, 500)
    cuenta_ahorros = CuentaAhorros("Miguel Sánchez", 2000, 5)
    
    cuentas = [cuenta_corriente, cuenta_ahorros]
    
    print("Saldo inicial de las cuentas:")
    for cuenta in cuentas:
        print(f"{cuenta.titular}: ${cuenta.saldo}")
    
    print("\nIntentando retirar $1200 de la cuenta corriente:")
    cuenta_corriente.retirar(1200)
    print(f"Saldo después del retiro: ${cuenta_corriente.saldo}")
    
    print("\nAplicando interés a la cuenta de ahorros:")
    cuenta_ahorros.aplicar_interes()
    print(f"Saldo después de aplicar interés: ${cuenta_ahorros.saldo}")

       