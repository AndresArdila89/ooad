class GuitarSpec:
    
    def __init__(self, builder, model, typee, backWood, topWood):
        self.builder = builder
        self.model = model
        self.type = typee
        self.backWood = backWood
        self.topWood = topWood

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
    
        