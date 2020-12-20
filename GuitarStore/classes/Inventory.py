from .Guitar import Guitar
class Inventory:
    
    def __init__(self):
        self.guitars = []
        print('Object created')

    def addGuitar(self, serialNumber, price,builder,model,typee,backWood,topWood):
        newGuitar = Guitar(serialNumber, price,builder,model,typee,backWood,topWood)
        self.guitars.append(newGuitar)
    
    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerial() == serialNumber:
                print("guitar found")
                
                return guitar
            else:
                print("No guitar in the system")
  
    def search(self, searchGuitar):
        for guitar in self.guitars:
            builder = searchGuitar.getBuilder()
            if (builder != None) and (not builder == '') and (not builder == guitar.getBuilder()):
                continue
            model = searchGuitar.getModel()
            if (model != None) and (not model == '') and (not model == guitar.getModel()):
                continue
            typee = searchGuitar.getType()
            if (typee != None) and (not typee == '') and (not typee == guitar.getType()):
                continue
            backWood = searchGuitar.getBackWood()
            if (backWood != None) and (not backWood == '') and (not backWood == guitar.getBackWood()):
                continue
            topWood = searchGuitar.getTopWood()
            if (topWood != None) and (not topWood == '') and (not topWood == guitar.getTopWood()):
                continue
        return False