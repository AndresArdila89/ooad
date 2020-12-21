from enum import Enum

class Builder(Enum):
    FENDER = 0
    MARTIN = 1
    GIBSON = 2
    COLLINGS = 3
    OLSON = 4
    RYAN = 5
    PRS = 6
    ANY = 7

    def __str__(self):
        builder = {
            self.FENDER : "Fender",
            self.MARTIN : "Martin",
            self.GIBSON : "Gibson",
            self.COLLINGS : "Collings",
            self.OLSON : "Olson",
            self.RYAN : "Ryan",
            self.PRS : "PRS",
            self.ANY : "any",
        }

        return builder.get(self)

