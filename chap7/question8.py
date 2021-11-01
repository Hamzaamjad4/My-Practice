class Stopwatch:
    def __init__(self,startTime=0,endTime=10):
        self.startTime = startTime
        self.endTime =endTime

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def getElapsedTime(self):
        elapsedTime = None;

        if (self.endTime != None):
            elapsedTime = (self.endTime - self.startTime) * 1000

        return elapsedTime

p1=Stopwatch()
print(p1.getElapsedTime())