# Code,Name,Type,Intelligence,Charisma,Fitness,Energy,Stress,Money,Flavor Text
# type is not needed because all these events will be passive... easier to make separate classes than just one big mess
import csv
from ActiveRandomEventChoice import ActiveRandomEventChoice

class ActiveRandomEvent():

    def __init__(self, code, name, eventType, desc, flavorText):
        self.code = code
        self.name = name
        self.eventType = eventType
        self.desc = desc
        self.flavorText = flavorText
        self.choiceList = {} #list of choices that the player can choose from

    def __repr__(self):
        return "Name: " + self.name + "\nDescription: " + self.desc +  "\nflavorText: " + self.flavorText + "\n"

    def printChoices(self):
        for i in range(len(self.choiceList)):
            print(self.choiceList[i])
        

#class end

def addRandomEvents(fileName):
        randomEvents = {}
        # open the csv file fileName and read from it
        with open(fileName, encoding="utf8", newline = '') as csvfile:
            r = csv.DictReader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            i = -1 # counter for list of random events
            j = 0 # counter for choices after a question
            for row in r:
                # for each row in csvFile, append the class activity to the array activities
                if(row["Type"] == "Question"):
                    i+= 1
                    j = 0
                    randomEvents[i] = ActiveRandomEvent( 
                        str(row["Code"]),
                        str(row["Name"]), 
                        str(row["Type"]),
                        str(row["Description"]),
                        str(row["Flavor Text"]),
                    )
                else:
                    randomEvents[i].choiceList[j] = ActiveRandomEventChoice( 
                        str(row["Code"]),
                        str(row["Name"]), 
                        str(row["Type"]),
                        str(row["Description"]),
                        int(row["Intelligence"]),
                        int(row["Charisma"]),
                        int(row["Fitness"]), 
                        int(row["Energy"]),
                        int(row["Stress"]),
                        int(row["Money"]),
                        str(row["Intelligence Check"]),
                        str(row["Charisma Check"]),
                        str(row["Fitness Check"]),
                        str(row["Energy Check"]),
                        str(row["Stress Check"]),
                        str(row["Money Check"]),
                        str(row["Flavor Text"]),
                    )
                    j += 1
        return randomEvents

if __name__ == "__main__":
    randomEventList = addRandomEvents("testActiveRandomEvent.csv")
    print(randomEventList)
    # randomEventList[0].printChoices()

# instead of storing each thing individually, each active event object will have its
# attributes but also store a list of the available options