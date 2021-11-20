import csv
from ClassActivity import ClassActivity

class ClassEvent(ClassActivity):
    def __init__(self, code, name, desc, schedTime, mon, tues, wed, thurs, fri, sat, sun, timeCost, knowledge, charisma, fitness, stress, energy, money, flavorText):
        super().__init__(code, name, desc, knowledge, charisma, fitness, stress, energy, money, flavorText)
        self.timeCost = timeCost
        self.schedTime = schedTime
        self.schedDays = [mon, tues, wed, thurs, fri, sat, sun]

    def missedEvent(self):
        return self

    def __repr__(self):
        return "Name: " + self.name + " \n" + "Description: " + self.desc + "\n" + "Scheduled Time: " + self.schedTime + "; Scheduled Day: " + "Filler text \n"  + "Time Cost: " + str(self.timeCost) + "\n" + "Knowledge: " + str(self.knowledge) + "\n" + "Charisma: "+ str(self.charisma) + "\n" + "Fitness: " + str(self.fitness) + "\n" + "Energy: " + str(self.energy) + "\n" + "Stress: " + str(self.stress) + "\n" + "Money: " + str(self.money) + "\n" + "Flavor Text: " + str(self.flavorText) + "\n\n"



def addEvents(fileName):
        events = {}
        # open the csv file fileName and read from it
        with open(fileName, encoding="utf8", newline = '') as csvfile:
            r = csv.DictReader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            i = 0
            for row in r:
                # for each row in csvFile, append the class activity to the array activities
                events[i] = ClassEvent( 
                    str(row["Code"]),
                    str(row["Name"]), 
                    str(row["Description"]), 
                    str(row["Scheduled Time"]),
                    str(row["Monday"]),
                    str(row["Tuesday"]),
                    str(row["Wednesday"]),
                    str(row["Thursday"]),
                    str(row["Friday"]),
                    str(row["Saturday"]),
                    str(row["Sunday"]),
                    int(row["Time Cost"]), 
                    int(row["Knowledge"]),
                    int(row["Charisma"]),
                    int(row["Fitness"]), 
                    int(row["Energy"]),
                    int(row["Stress"]),
                    int(row["Money"]),
                    str(row["Flavor Text"]),
                    
                )
                i += 1
        return events

if __name__ == "__main__":
    eventList = addEvents("testClassEvent.csv")
    print(eventList)
