import math


class WorkStationJob:
    def __init__(self, jobNumber, arrivalTime, timeNeeded):
        self.jobNumber = jobNumber
        self.arrivalTime = arrivalTime
        self.timeNeeded = timeNeeded

    startTime = -1
    limit1Start = -math.inf
    limit1End = -math.inf
    limit2Start = -math.inf
    limit2End = -math.inf

    def checkArrivalState(self, time):
        if time >= self.arrivalTime:
            return True
        else:
            return False

    def checkAvailability(self, time):
        if (time < self.limit1End and time + self.timeNeeded > self.limit1Start) or \
                (time < self.limit2End and time + self.timeNeeded > self.limit2Start):
            return False
        else:
            return True
