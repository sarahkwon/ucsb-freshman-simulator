import csv

class ClassActivity:

    def __init__(self, name, desc, timeCost, statModifiers, resourceModifiers, flavorText):
        self.name = name
        self.desc = desc
        self.timeCost = timeCost
        self.statModifiers = statModifiers
        self.resourceModifiers = resourceModifiers
        self.flavorText = flavorText
    
    def __repr__(self):
        return "Name: " + self.name + ": \n" + "Description: " + self.desc + "\n" + "Time Cost: " + str(self.timeCost) + "\n" + "Stat Modifiers: " + self.statModifiers + "\n" +"Resource Modifiers: " + self.resourceModifiers + "\n" +"Flavor Text: " + self.flavorText + "\n"

def addActivities(fileName):
        activities = {}
        # open the csv file fileName and read from it
        with open(fileName, newline = '') as csvfile:
            r = csv.DictReader(csvfile, delimiter=',')
            i = 0
            for row in r:
                # for each row in csvFile, append the class activity to the array activities
                activities[row["name"]] = ClassActivity(
                    str(row["name"]), 
                    str(row["description"]), 
                    int(row["timeCost"]), 
                    str(row["statModifiers"]), 
                    str(row["resourceModifiers"]),
                    str(row["flavor"])
                )
                i += 1
        return activities