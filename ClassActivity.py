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
