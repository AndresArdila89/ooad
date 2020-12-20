from Airplane import Airplane


Airplane.getSpeed


class Jet(Airplane):
    def setSpeed(self,speed):
        self.speed = speed * 10
    
    def acceletate(self):
        self.setSpeed(self.getSpeed() * 2)


    def diplayInfo(self):
        print("speed", self.speed)



    