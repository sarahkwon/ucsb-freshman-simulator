# Code,Name,Type,Intelligence,Charisma,Fitness,Energy,Stress,Money,Flavor Text
# type is not needed because all these events will be passive... easier to make separate classes than just one big mess
import csv
from ClassActivity import ClassActivity

class PassiveRandomEvent(ClassActivity):

    def __init__(self, code, name, desc, eventType, intelligence, charisma, fitness, energy, stress, money, flavorText):
        super().__init__(code, name, desc, intelligence, charisma, fitness, energy, stress, money, flavorText)
        self.eventType = eventType
        

    def __repr__(self):
        return "Name: " + self.name + "\nDescription: " + self.desc + "\nIntelligence: " + str(self.intelligence) + "\nCharisma: " + str(self.charisma) + "\nFitness: " + str(self.fitness) +  "\nEnergy: " + str(self.energy) + "\nStress: " + str(self.stress) + "\nMoney: " + str(self.money) + "\nflavorText: " + self.flavorText + "\n\n"

#class end

def addRandomEvents(fileName):
        randomEvents = {}
        # open the csv file fileName and read from it
        with open(fileName, encoding="utf8", newline = '') as csvfile:
            r = csv.DictReader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            i = 0
            for row in r:
                # for each row in csvFile, append the class activity to the array activities
                randomEvents[i] = PassiveRandomEvent( 
                    str(row["Code"]),
                    str(row["Name"]), 
                    "fill description",
                    str(row["Type"]),
                    int(row["Intelligence"]),
                    int(row["Charisma"]),
                    int(row["Fitness"]), 
                    int(row["Energy"]),
                    int(row["Stress"]),
                    int(row["Money"]),
                    str(row["Flavor Text"]),
                )
                i += 1
        return randomEvents

if __name__ == "__main__":
    randomEventList = addRandomEvents("Events_random_passive.csv")
    print(randomEventList)