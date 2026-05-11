#Ejercicio 1: Sistema de Gestión de Empleados

# Crea un sistema que gestione diferentes tipos de empleados en una empresa: Empleado, Gerente y Desarrollador.
#    Empleado: Clase base con atributos encapsulados (nombre, salario_base) y métodos para calcular el salario.
#    Gerente: Hereda de Empleado y añade un atributo bono. El salario se calcula como salario_base + bono.
#    Desarrollador: Hereda de Empleado y añade un atributo horas_extra. El salario se calcula como 
#       salario_base + (horas_extra * 50).
#    Implementa el polimorfismo en el método calcular_salario() para cada tipo de empleado.

import os
os.system("cls")

class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono
    
    def calcular_salario(self):
        return super().calcular_salario() + self.bono

# Clase Desarrollador que hereda de Empleado
class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, horas_extra):
        super().__init__(nombre, salario_base)
        self.__horasextra = horas_extra
    
    def calcular_salario(self):
        return super().calcular_salario() + (self.__horasextra * 50)

# Ejemplo
if __name__ == "__main__":
    
    empleado = Empleado("Juan Pérez", 3000)
    gerente = Gerente("Ana García", 4000, 500)
    desarrollador = Desarrollador("Carlos López", 3500, 20)
    
    empleados = [empleado, gerente, desarrollador]
    
    print("Salarios de los empleados:")
    for emp in empleados:
        print(f"{emp.nombre}: ${emp.calcular_salario()}")

