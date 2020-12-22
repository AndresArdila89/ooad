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
        guitarsList = []

        for guitar in self.guitars:
            
            if guitar.getBuilder() != searchGuitar.getBuilder():
                continue
            model = searchGuitar.getModel()
            if (model == None) or (model == '') or (model.lower() != guitar.getModel().lower()):                
                continue
            if guitar.getType() != searchGuitar.getType():
                continue
            if guitar.getBackWood() != searchGuitar.getBackWood():
                continue
            if guitar.getTopWood() != searchGuitar.getTopWood():
                continue
            guitarsList.append(guitar)
        
        return guitarsList