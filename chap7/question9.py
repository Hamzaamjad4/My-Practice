import datetime
import time
class Time:
    def __init__(self, created=None):
        self.created = created or time.time()

    def getHoure(self):
        return self.created
    print(time.time())
    # def getMinutes(self):
    #     return self.minutes
    # def getSeconds(self):
    #     return self.seconds
    # def getTime(self):
    #     return self.hour,self.minutes,self.seconds
    # def getElapsedTime(self):
    #     elapsedTime = None;
    #
    #     if (self.endTime != None):
    #         elapsedTime = (self.endTime - self.startTime) * 1000
    #
    #     return elapsedTime
p1=Time()
print(p1.getHoure())
