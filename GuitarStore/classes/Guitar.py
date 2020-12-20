class Guitar:
    'Common base class for all Guitars'
    
    def __init__(self, serialNumber, price,builder,model,typee,backWood,topWood):
        self.serialNumber = serialNumber
        self.price = price
        self.builder = builder
        self.model = model
        self.type = typee
        self.backWood = backWood
        self.topWood = topWood

    def getSerial(self):
        return self.serialNumber
    
    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price
    
    def getBuilder(self):
        return self.builder

    def getModel(self):
        return self.model

    def getType(self): 
        return self.type

    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood
        
    
