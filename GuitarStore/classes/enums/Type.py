from enum import Enum
class Type(Enum):
    ACUSTIC = 0
    ELECTRIC = 1

    def __str__(self):
        guitarType = {
            self.ELECTRIC : "Electric",
            self.ACUSTIC : "Acustic"
        }
        return guitarType.get(self)