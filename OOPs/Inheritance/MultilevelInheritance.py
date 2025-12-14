class Factory:
    def __init__(self,material,zip):
        self.material = material
        self.zip = zip

class Factorymumbai(Factory):
    def __init__(self, material, zip,color):
        super().__init__(material, zip)
        self.color = color 

class FactoryPune(Factorymumbai):
    def __init__(self, material, zip, color,pockets):
        super().__init__(material, zip, color)
        self.pockets = pockets 

obj = FactoryPune()