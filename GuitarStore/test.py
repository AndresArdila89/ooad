from classes.Guitar import Guitar
from classes.Inventory import Inventory
from classes.enums.Type import Type
from classes.enums.Builder import Builder
from classes.enums.Wood import Wood




inventory = Inventory()
inventory.addGuitar("V95693",1499.95,Builder.FENDER,'Stratocastor',Type.ELECTRIC,Wood.ALDER,Wood.ALDER)
inventory.addGuitar("V9512",1549.95,Builder.FENDER,'Stratocastor',Type.ELECTRIC,Wood.ALDER,Wood.ALDER)
inventory.addGuitar("V9513",1549.95,Builder.FENDER,'Stratocastor',Type.ACUSTIC,Wood.ALDER,Wood.ALDER)
inventory.addGuitar("V9515",1549.95,Builder.GIBSON,'Stratocastor',Type.ELECTRIC,Wood.ALDER,Wood.ALDER)

whatErinLikes = Guitar("",0,Builder.FENDER,'stratocastor',Type.ELECTRIC,Wood.ALDER,Wood.ALDER)

erinGuitars = inventory.search(whatErinLikes)
if not erinGuitars:
    print("Sorry, Erin, we have nothing for you")
else:
    print("Erin, you might like this guitars:")
    for guitar in erinGuitars:
        print(f"Model: {guitar.getModel()}, TopWood: {guitar.getTopWood()}, BackWood: {guitar.getBackWood()} Price: {guitar.getType()}")
