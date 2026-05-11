# Ejercicio 2: Sistema de Figuras Geométricas

#   Crea un sistema para calcular el área de diferentes figuras geométricas: Círculo, Rectángulo y Triángulo.
#   Figura: Clase base con un método calcular_area() que debe ser implementado por las
#       clases hijas.
#   Círculo, Rectángulo y Triángulo: Heredan de Figura e implementan calcular_area()
#       según su fórmula específica.
#   Usa polimorfismo para calcular el área de cualquier figura sin conocer su tipo.

import os
import math
os.system("cls")

# Clase base Figura
class Figura:
    def calcular_area(self):
        raise NotImplementedError("Las clases hijas deben implementar calcular_area()")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

# Ejemplo 
if __name__ == "__main__":
    circulo = Circulo(5)
    rectangulo = Rectangulo(10, 4)
    triangulo = Triangulo(6, 8)
    
    figuras = [circulo, rectangulo, triangulo]
    
    print("Áreas de las figuras geométricas:")
    print(f"Círculo (radio=5): {circulo.calcular_area()} ")
    print(f"Rectángulo (base=10, altura=4): {rectangulo.calcular_area()}")
    print(f"Triángulo (base=6, altura=8): {triangulo.calcular_area()} ")
    
    print("\nCalculando áreas usando polimorfismo:")
    for i, figura in enumerate(figuras, 1):
        print(f"Figura {i}: {figura.calcular_area()} ")