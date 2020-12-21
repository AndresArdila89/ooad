from classes.Guitar import Guitar
from classes.Inventory import Inventory
from classes.enums.Type import Type
from classes.enums.Builder import Builder
from classes.enums.Wood import Wood




inventory = Inventory()
inventory.addGuitar("V95693",1499.95,'Fender','Stratocastor','Electric','Alder','Alder')

whatErinLikes = Guitar("",0,Builder.FENDER,'stratocastor',Type.ELECTRIC,Wood.ALDER,Wood.ALDER)

erinGuitar = inventory.search(whatErinLikes)
if erinGuitar:
    print(f"Model {whatErinLikes.getModel()}, Price {whatErinLikes.getType()}")
else:
    print("Sorry, Erin, we have nothing for you")

