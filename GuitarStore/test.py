from classes.Guitar import Guitar
from classes.Inventory import Inventory


inventory = Inventory()
inventory.addGuitar("V95693",1499.95,'Fender','Stratocastor','Electric','Alder','Alder')

whatErinLikes = Guitar("",0,'Fender','Stratocastor','Electric','Alder','Alder')

erinGuitar = inventory.search(whatErinLikes)
if erinGuitar:
    print("Model {}, Price {}", whatErinLikes.getModel(), whatErinLikes.getPrice)
else:
    print("Sorry, Erin, we have nothing for you")

