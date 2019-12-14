import math


class WorkStationJob:
    def __init__(self, jobNumber, arrivalTime, timeNeeded):
        self.jobNumber = jobNumber
        self.arrivalTime = arrivalTime
        self.timeNeeded = timeNeeded

    startTime = -1
    limit1Start = 0
    limit1End = 0
    limit2Start = 0
    limit2End = 0

    def checkArrivalState(self, time1):
        if time1 >= self.arrivalTime:
            return True
        else:
            return False

    def checkAvailability(self, time1):
        if (time1 < self.limit1End and time1 + self.timeNeeded > self.limit1Start) or \
                (time1 < self.limit2End and time1 + self.timeNeeded > self.limit2Start):
            return False
        else:
            return True
