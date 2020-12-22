from classes.Guitar import Guitar
from classes.Inventory import Inventory
from classes.enums.Type import Type
from classes.enums.Builder import Builder
from classes.enums.Wood import Wood
from classes.GuitarSpec import GuitarSpec




inventory = Inventory()
inventory.addGuitar("V95693",1499.95,GuitarSpec(Builder.FENDER,'Stratocastor',Type.ELECTRIC,Wood.ALDER,Wood.ALDER))
inventory.addGuitar("V9512",1549.95,GuitarSpec(Builder.FENDER,'Stratocastor',Type.ELECTRIC,Wood.ALDER,Wood.ALDER))
inventory.addGuitar("V9513",1549.95,GuitarSpec(Builder.FENDER,'Stratocastor',Type.ACUSTIC,Wood.ALDER,Wood.ALDER))
inventory.addGuitar("V9515",1549.95,GuitarSpec(Builder.GIBSON,'Stratocastor',Type.ELECTRIC,Wood.ALDER,Wood.ALDER))

whatErinLikes = GuitarSpec(Builder.FENDER,'stratocastor',Type.ACUSTIC,Wood.ALDER,Wood.ALDER)

erinGuitars = inventory.search(whatErinLikes)
if not erinGuitars:
    print("Sorry, Erin, we have nothing for you")
else:
    print("Erin, you might like this guitars:")
    for guitar in erinGuitars:
        spec = guitar.getSpec()
        print(f"Model: {spec.getModel()}, TopWood: {spec.getTopWood()}, BackWood: {spec.getBackWood()} Price: {spec.getType()}")
