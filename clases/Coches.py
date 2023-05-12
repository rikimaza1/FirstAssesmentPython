from abc import ABC, abstractmethod

class Coches(ABC):
    def __init__(self, fabricante, anyo, modelo):
        self.fabricante = fabricante
        self.anyo = anyo
        self.modelo = modelo

    @abstractmethod
    def descripcion(self):
        pass

class Ford(Coches):
    def __init__(self, fabricante, anyo, modelo, color):
        super().__init__(fabricante, anyo, modelo)
        self.color = color

    def descripcion(self):
        print(f"Este es un Ford {self.modelo} de color {self.color} fabricado en {self.anyo} por {self.fabricante}.")

class Toyota(Coches):
    def __init__(self, fabricante, anyo, modelo, num_puertas):
        super().__init__(fabricante, anyo, modelo)
        self.num_puertas = num_puertas

    def descripcion(self):
        print(f"Este es un Toyota {self.modelo} de {self.num_puertas} puertas fabricado en {self.anyo} por {self.fabricante}.")

class Honda(Coches):
    def __init__(self, fabricante, anyo, modelo, tipo_transmision):
        super().__init__(fabricante, anyo, modelo)
        self.tipo_transmision = tipo_transmision

    def descripcion(self):
        print(f"Este es un Honda {self.modelo} con transmisión {self.tipo_transmision} fabricado en {self.anyo} por {self.fabricante}.")