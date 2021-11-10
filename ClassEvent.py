from ClassActivity import ClassActivity

class ClassEvent(ClassActivity):
    def __init__(self, name, desc, timeCost, statModifiers, resourceModifiers, flavorText, time, day):
        super().__init__(name, desc, timeCost, statModifiers, resourceModifiers, flavorText)
        self.time = time
        self.day = day

    def missedEvent(self):
        return self