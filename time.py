class Time:
    def __init__ (self):
        self.currentTime = 1500
    
    def changeTime(self, amount):
        if amount > self.currentTime:
            return False
        else:
            self.currentTime = self.currentTime - amount
