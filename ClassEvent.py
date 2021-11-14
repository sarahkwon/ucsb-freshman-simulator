from ClassActivity import ClassActivity

class ClassEvent(ClassActivity):
    def __init__(self, name, desc, timeCost, intelligence, charisma, fitness, resourceModifiers, flavorText, time, day):
        super().__init__(name, desc, timeCost, intelligence, charisma, fitness, resourceModifiers, flavorText)
        self.time = time
        self.day = day

    def missedEvent(self):
        return self