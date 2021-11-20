import csv
from ClassActivity import ClassActivity

class ClassEvent(ClassActivity):
    def __init__(self, code, name, desc, mon, tues, wed, thurs, fri, sat, sun, knowledge, charisma, fitness, stress, money, flavorText):
        super().__init__(code, name, desc, knowledge, charisma, fitness, 0, stress, money, flavorText)
        self.schedDays = [mon, tues, wed, thurs, fri, sat, sun]

    def missedEvent(self):
        return self

    def __repr__(self):
        return "Name: " + self.name + " \n" + "Description: " + self.desc + "\n" + "Scheduled Days: " + "Filler text \n" + "Knowledge: " + str(self.knowledge) + "\n" + "Charisma: "+ str(self.charisma) + "\n" + "Fitness: " + str(self.fitness) + "\n" + "Stress: " + str(self.stress) + "\n" + "Money: " + str(self.money) + "\n" + "Flavor Text: " + str(self.flavorText) + "\n\n"



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
                    int(row["Monday"]),
                    int(row["Tuesday"]),
                    int(row["Wednesday"]),
                    int(row["Thursday"]),
                    int(row["Friday"]),
                    int(row["Saturday"]),
                    int(row["Sunday"]),
                    int(row["Knowledge"]),
                    int(row["Charisma"]),
                    int(row["Fitness"]), 
                    int(row["Stress"]),
                    int(row["Money"]),
                    str(row["Flavor Text"]),
                    
                )
                i += 1
        return events

if __name__ == "__main__":
    eventList = addEvents("Scheduled Events.csv")
    print(eventList)
