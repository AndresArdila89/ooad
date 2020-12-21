from enum import Enum

class Wood(Enum):
    INDIAN_ROSEWOOD = 0
    BRAZILLIAN_ROSEWOOD = 1
    MOHOGANY = 2
    MAPLE = 3
    COCOBOLO = 4
    CEDAR = 5
    ADIRONDACK =6
    ALDER = 7 
    SITKA = 8

    def __str__(self):
        wood = {
            self.INDIAN_ROSEWOOD : "Indian rosewood",
            self.BRAZILLIAN_ROSEWOOD : "Brazillian Rosewood",
            self.MOHOGANY : "Mohogany",
            self.MAPLE : "Maple",
            self.COCOBOLO : "Cocobolo",
            self.CEDAR : "Cedar",
            self.ADIRONDACK : "Adirondack",
            self.ALDER : "Alder",
            self.SITKA : "Sitka",

        }
        return wood.get(self)