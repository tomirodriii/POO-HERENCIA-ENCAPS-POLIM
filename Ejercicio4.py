#Ejercicio 4: Sistema de Vehículos
#   Crea un sistema para gestionar diferentes tipos de vehículos: Vehículo, Automóvil y Motocicleta.
#   Vehículo: Clase base con atributos encapsulados (marca, modelo, año) y un método describir() que 
#             devuelve una descripción básica.
#   Automóvil: Hereda de Vehículo y añade un atributo puertas. El método describir() debe
#              incluir el número de puertas.
#   Motocicleta: Hereda de Vehículo y añade un atributo cilindrada. El método describir()
#                debe incluir la cilindrada.
#   Usa polimorfismo para llamar al método describir() en una lista de vehículos.

import os 
os.system("cls")

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def describir(self):
        return f"{self.marca} {self.modelo} ({self.año})"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas
    
    def describir(self):
        return f"{super().describir()} - {self.puertas} puertas"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def describir(self):
        return f"{super().describir()} - {self.cilindrada} cc"
    
# Ejemplo de uso para demostrar polimorfismo

if __name__ == "__main__":
    automovil = Automovil("Toyota", "Corolla", 2020, 4)
    motocicleta = Motocicleta("Honda", "CBR500R", 2019, 500)
    
    vehiculos = [automovil, motocicleta]
    
    print("Descripción de los vehículos:")
    for vehiculo in vehiculos:
        print(vehiculo.describir())
        