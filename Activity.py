import csv

class Activity:

    def __init__(self, code, name, desc, intelligence, charisma, fitness, energy, stress, money, flavorText):
        self.code = code
        self.name = name
        self.desc = desc
        self.intelligence = intelligence
        self.charisma = charisma
        self.fitness = fitness
        self.energy = energy
        self.stress = stress
        self.money = money
        self.flavorText = flavorText
    
    def __repr__(self):
        return "Name: " + self.name + ": \n" + "Description: " + self.desc +"\n" + "Intelligence: " + str(self.intelligence) + "\n" + "Charisma: "+ str(self.charisma) + "\n" + "Fitness: " + str(self.fitness) + "\n" + "Energy: " + str(self.energy) + "\nStress: " + str(self.stress) + "\n" + "Money: " + str(self.money) + "\n" +"Flavor Text: " + self.flavorText + "\n\n"

def addActivities(fileName):
        activities = {}
        # open the csv file fileName and read from it
        with open(fileName, encoding="utf8", newline = '') as csvfile:
            r = csv.DictReader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            i = 0
            for row in r:
                # for each row in csvFile, append the class activity to the array activities
                activities[i] = Activity( 
                    str(row["Code"]),
                    str(row["Name"]), 
                    str(row["Description"]),  
                    int(row["Intelligence"]),
                    int(row["Charisma"]),
                    int(row["Fitness"]), 
                    int(row["Energy"]),
                    int(row["Stress"]),
                    int(row["Money"]),
                    str(row["Flavor Text"])
                )
                i += 1
        return activities

activities = addActivities("Activities.csv")

if __name__ == "__main__":
    a = addActivities('Activities.csv')
    print(a)