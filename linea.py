class Linea:

    def __init__(self, laletra, b, d):
        self.letra = laletra
        self.espacio = b
        self.dimension = d

    def __str__(self):
        return f"{self.letra}{self.espacio*(self.dimension-2)}{self.letra}\n"
    
    
    


