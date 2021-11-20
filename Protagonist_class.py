#protagonist.py'
import ClassActivity as Activity
import ClassEvent as Event
from   ClassActivity import activities

class Protagonist():
    def __init__(self, your_name, your_major):
        self.name = your_name
        self.major = your_major
        self.intelligence = 0
        self.charisma = 5
        self.fitness = 1
        self.xp = 1
        self.stress = 0 #0 - 100%
        self.energy = 100 #0 - 100%
        self.money = 500


    # update player class given a class activity
    def updateStats(self, activity):
        self.updateIntelligence(activity.intelligence)
        self.updateCharisma(activity.charisma)
        self.updateFitness(activity.fitness)
        self.updateStress(activity.stress)
        self.updateMoney(activity.money)

    def updateStats(self, event):
        self.updateIntelligence(event.intelligence)
        self.updateCharisma(event.charisma)
        self.updateFitness(event.fitness)
        self.updateEnergy(event.energy)
        self.updateStress(event.stress)
        self.updateMoney(event.money)


    # basic set functions for class    
    def updateIntelligence(self, amt):
        self.intelligence += amt
        if (self.intelligence < 0):
            self.intelligence = 0

    def updateCharisma(self, amt):
        self.charisma += amt
        if (self.charisma < 0):
            self.charisma = 0

    def updateFitness(self, amt):
        self.fitness += amt
        if (self.fitness < 0):
            self.fitness = 0

    def updateXP(self, amt):
        self.xp += amt

    def updateStress(self, amt):
        self.stress += amt
        if (self.stress > 100):
            self.stress = 100
        if (self.stress < 0):
            self.stress = 0

    def updateEnergy(self, amt):
        self.energy += amt
        if (self.energy > 100):
            self.energy = 100
        if (self.energy < 0):
            self.energy = 0

    def updateMoney(self, amt):
        self.money += amt
        
    def printStats(self, args):
        arg = activities[args]
        psign = "(+"
        msign = "("
        nsign = ""
        lbracket = '('
        rbracket = ')'

        self.updateStress(arg.stress)
        self.updateEnergy(arg.energy)
        self.updateMoney(arg.money)
        self.updateIntelligence(arg.intelligence)
        self.updateFitness(arg.fitness)
        self.updateCharisma(arg.charisma)
        print(
            f"""
    {self.name}
    Major: {self.major}
|----RESOURCES----<>
| Stress   | {self.stress:<3} {psign if arg.stress > 0 else nsign}{lbracket if arg.stress < 0 else nsign}{arg.stress if arg.stress != 0 else nsign:>1}{rbracket if arg.stress != 0 else nsign}
| Energy   | {self.energy:<3} {psign if arg.energy > 0 else nsign}{lbracket if arg.energy < 0 else nsign}{arg.energy if arg.energy != 0 else nsign:>1}{rbracket if arg.energy != 0 else nsign}
| Money    |${self.money:<3} {psign if arg.money > 0 else nsign}{lbracket if arg.money < 0 else nsign}{arg.money if arg.money != 0 else nsign:>1}{rbracket if arg.money != 0 else nsign}
|------STATS------<>
| XP       | {self.xp:<3} ({200:>1})
| Intel    | {self.intelligence:<3} {psign if arg.intelligence > 0 else nsign}{arg.intelligence if arg.intelligence != 0 else nsign:>1}{rbracket if arg.intelligence != 0 else nsign}
| Fitness  | {self.fitness:<3} {psign if arg.fitness > 0 else nsign}{arg.fitness if arg.fitness != 0 else nsign:>1}{rbracket if arg.fitness != 0 else nsign}
| Charisma | {self.charisma:<3} {psign if arg.charisma > 0 else nsign}{arg.charisma if arg.charisma != 0 else nsign:>1}{rbracket if arg.charisma != 0 else nsign}
|------------------<>
            """
        )

if __name__ == "__main__":
    test = Protagonist("John", "cs")
    testActivity = Activity.ClassActivity("test_code", "test_activity", "this is a test activity", 1, 1, 1,-1, -1, -1, "flavor text")
    test.updateStats(testActivity)
    print(test.stress)

    testEvent = Event.ClassEvent("test_event", "test event name", "this is a test event", 1, 1, 1, 1, 1, 1, 1, 4, -1, -1, -1, -1, "flavor text")
    test.updateStats(testEvent)
    print(test.intelligence)