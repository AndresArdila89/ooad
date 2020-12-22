from .Guitar import Guitar
class Inventory:
    
    def __init__(self):
        self.guitars = []
        print('Object created')

    def addGuitar(self, serialNumber, price,spec):
        newGuitar = Guitar(serialNumber, price,spec)
        self.guitars.append(newGuitar)
    
    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerial() == serialNumber:
                print("guitar found")
                
                return guitar
            else:
                print("No guitar in the system")
  
    def search(self, searchSpec):
        guitarsList = []

        for guitar in self.guitars:
            guitarSpec = guitar.getSpec()

            if guitarSpec.getBuilder() != searchSpec.getBuilder():
                continue
            model = searchSpec.getModel()
            if (model == None) or (model == '') or (model.lower() != guitarSpec.getModel().lower()):                
                continue
            if guitarSpec.getType() != searchSpec.getType():
                continue
            if guitarSpec.getBackWood() != searchSpec.getBackWood():
                continue
            if guitarSpec.getTopWood() != searchSpec.getTopWood():
                continue
            guitarsList.append(guitar)
        
        return guitarsList