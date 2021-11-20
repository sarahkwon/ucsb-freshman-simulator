#protagonist.py'
import ClassActivity as Activity

class Protagonist():
    def __init__(self, your_name, your_major):
        self.name = your_name
        self.major = your_major
        self.s_Knowledge = 0
        self.s_Charisma = 5
        self.s_Fitness = 1
        self.s_XP = 1 
        self.r_stress = 0 #0 - 100%
        self.r_energy = 100 #0 - 100%
        self.r_money = 50 

    # update player class given a class activity
    def updateStats(self, activity):
        self.updateKnowledge(activity.intelligence)
        self.updateCharisma(activity.charisma)
        self.updateFitness(activity.fitness)
        self.updateEnergy(activity.energy)
        self.updateStress(activity.stress)
        self.updateMoney(activity.money)


    # basic set functions for class    
    def updateKnowledge(self, amt):
        self.s_Knowledge += amt
        if (self.s_Knowledge < 0):
            self.s_Knowledge = 0

    def updateCharisma(self, amt):
        self.s_Charisma += amt
        if (self.s_Charisma < 0):
            self.s_Charisma = 0

    def updateFitness(self, amt):
        self.s_Fitness += amt
        if (self.s_Fitness < 0):
            self.s_Fitness = 0

    def updateXP(self, amt):
        self.s_XP += amt

    def updateStress(self, amt):
        self.r_stress += amt
        if (self.r_stress > 100):
            self.r_stress = 100
        if (self.r_stress < 0):
            self.r_stress = 0

    def updateEnergy(self, amt):
        self.r_energy += amt
        if (self.r_energy > 100):
            self.r_energy = 100
        if (self.r_energy < 0):
            self.r_energy = 0

    def updateMoney(self, amt):
        self.r_money += amt

if __name__ == "__main__":
    test = Protagonist("John", "cs")
    testActivity = Activity.ClassActivity("test_code", "test_activity", "this is a test activity", 1, 1, 1, 1, -1, -1, -1, "flavor text")
    test.updateStats(testActivity)
    print(test.r_energy)