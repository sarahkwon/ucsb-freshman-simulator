class Resources:
    energyLevel = 0
    hungerLevel = 0 # 3 == full, 2 == satisfied, 1 == hungry, 0 == starving 
    stressLevel = 0
    money = 0 

    def __init__(self, energyLevel, hungerLevel, stressLevel, money):
        self.energyLevel = energyLevel
        self.hunger = hunger
        self.stress = stress
        self.money = money

    # do i need get statements in python? 

    def lowerEnergyLevel(amt): # multiplier to account for player's physical level? 
        energyLevel -= amt
        if (energyLevel < 0):
            energyLevel = 0
    
    def raiseEnergyLevel(amt):
        energyLevel += amt
        if (energyLevel > 100):
            energyLevel = 100

    def raiseHungerLevel():
        if (hungerLevel < 3):
            hungerLevel += 1

    def lowerHungerLevel():
        if (hungerLevel > 0):
            hungerLevel -= 1

    def raiseStressLevel(amt):
        stressLevel += amt
        if (stressLevel > 100):
            stressLevel = 100

    def lowerStressLevel(amt):
        stressLevel -= amt
        if (stressLevel < 0):
            stressLevel = 0

    def addMoney(amt):
        money += amt

    def loseMoney(amt):
        money -= amt