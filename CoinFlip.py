import random

class Coin:
    def __init__ (self):
        self.sideUp = "Tails"
    
    def toss(self):
        randomFlip = random.randrange(0,2)
        if randomFlip == 0:
            self.sideUp = "Tails"
        else:
            self.sideUp = "Heads"

coin = Coin()   #Create new instance of Coin (coin)
 
coin.toss()
print("\n Srineeta 1MJ19CS163")
print("The top of the coin shows: ", coin.sideUp, "\n")