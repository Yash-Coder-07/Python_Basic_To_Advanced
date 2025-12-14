class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    
    def show(self):
        print(f"Your Object details are {self.material}, {self.pockets}, {self.zips}")

# Self target object location 
reebok = Factory("Leather",3,2)
campus = Factory("Waterproof",4,3)

reebok.show()