class Guitar:
    'Common base class for all Guitars'
    
    def __init__(self, serialNumber, price,spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec

    def getSerial(self):
        return self.serialNumber
    
    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price
    
    def getSpec(self):
        return self.spec
    
    
