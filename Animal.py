class Animal():
    def __init__(self, numteeth, spots, weight):
        self.numteeth = numteeth
        self.spots = spots
        self.weight = weight
# create the inherited class with the Super Class called in the parenthesis
class Lion(Animal):
    
    def __init__(self, tail, numteeth, spots, weight):
        super().__init__(numteeth, spots, weight)
        self.tail = tail
    def type_lion(self):
        if self.weight < 80:
            print("this is a cub")
        elif self.weight < 120:
            print("this is a female")
        elif self.weight > 120:
            print("this is a male")
LION1 = Lion("White Lion", 15, "Yes", 70)
LION2 = Lion("White Lion", 30, "Yes", 95)
LION3 = Lion("White Lion", 30, "Yes", 130)
# run the methods
LION1.type_lion()
LION2.type_lion()
LION3.type_lion()

class Cheetah(Animal):
    
    def __init__(self, coat, numteeth, spots, weight):
        super().__init__(numteeth, spots, weight)
        self.coat = coat
    def type_Cheetah(self):
        if self.weight <80:
            print("this is a cub")
        elif self.weight <110:
            print("this is a female")
        elif self.weight <200:
            print("this is a male")
Cheetah1 = Cheetah("Tanzanian cheetah ", 25, "Yes", 75)
Cheetah2 = Cheetah("Tanzanian cheetah ", 32, "Yes", 99)
Cheetah3 = Cheetah("Tanzanian cheetah ", 40, "Yes", 130)
# run the methods
Cheetah1.type_Cheetah()
Cheetah2.type_Cheetah()
Cheetah3.type_Cheetah()





    
    

                



