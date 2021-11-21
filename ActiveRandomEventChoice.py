# Code,Name,Type,Intelligence,Charisma,Fitness,Energy,Stress,Money,Flavor Text
# type is not needed because all these events will be passive... easier to make separate classes than just one big mess
import csv
from Activity import Activity

class ActiveRandomEventChoice(Activity):

    def __init__(self, code, name, eventType, desc, intelligence, charisma, fitness, energy, stress, money, intelligenceCheck, charismaCheck, fitnessCheck, energyCheck, stressCheck, moneyCheck, flavorText):
        super().__init__(code, name, desc, intelligence, charisma, fitness, energy, stress, money, flavorText)
        self.eventType = eventType
        self.intelligenceCheck = intelligenceCheck
        self.charismaCheck = charismaCheck
        self.fitnessCheck = fitnessCheck
        self.energyCheck = energyCheck
        self.moneyCheck = moneyCheck
        

    def __repr__(self):
        return "Name: " + self.name + "\nDescription: " + self.desc + "\nIntelligence: " + str(self.intelligence) + "\nCharisma: " + str(self.charisma) + "\nFitness: " + str(self.fitness) +  "\nEnergy: " + str(self.energy) + "\nStress: " + str(self.stress) + "\nMoney: " + str(self.money) + "\nflavorText: " + self.flavorText + "\n\n"

#class end

if __name__ == "__main__":
    print("haha")