from linea import Linea

class Cuadrado:

    def __init__(self, letra, dimension):
        self.lineaA = Linea(letra,letra, dimension)
        self.lineaB = Linea(letra, " ", dimension)
        self.dimension = dimension

        
    def __str__(self):
        resultado = str(self.lineaA)
        for i in range(self.dimension-2):
            resultado += str(self.lineaB)
        resultado += str(self.lineaA)
        return resultado



