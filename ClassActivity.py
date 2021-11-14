import csv

class ClassActivity:

    def __init__(self, code, name, desc, timeCost, intelligence, charisma, fitness, energy, stress, money, flavorText):
        self.code = code
        self.name = name
        self.desc = desc
        self.timeCost = timeCost
        self.intelligence = intelligence
        self.charisma = charisma
        self.fitness = fitness
        self.energy = energy
        self.stress = stress
        self.money = money
        self.flavorText = flavorText
    
    def __repr__(self):
        return "Name: " + self.name + ": \n" + "Description: " + self.desc + "\n" + "Time Cost: " + str(self.timeCost) + "\n" + "Intelligence: " + str(self.intelligence) + "\n" + "Charisma: "+ str(self.charisma) + "\n" + "Fitness: " + str(self.fitness) + "Stress: " + self.stress + "\n" + "Energy: " + self.energy + "\n" + "Money: " + self.money + "\n" +"Flavor Text: " + self.flavorText + "\n"

def addActivities(fileName):
        activities = {}
        # open the csv file fileName and read from it
        with open(fileName, newline = '') as csvfile:
            r = csv.DictReader(csvfile, delimiter=',')
            i = 0
            for row in r:
                # for each row in csvFile, append the class activity to the array activities
                activities[i] = ClassActivity( 
                    str(row["Code"]),
                    str(row["Name"]), 
                    str(row["Description"]), 
                    str(row["Time Cost"]), 
                    str(row["Intelegence"]),
                    str(row["Charisma"]),
                    str(row["Fitness"]), 
                    str(row["Energy"]),
                    str(row["Stress"]),
                    str(row["Money"]),
                    str(row["Flavor Text"])
                )
                i += 1
        return activities

if __name__ == "__main__":
    a = addActivities('test.csv')
    print(a)