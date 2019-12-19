import math


class SimulatedAnnealing:
    def __init__(self, newJobOption):
        self.newJobOption = newJobOption

    probabilityIntervalStart = 0
    probabilityIntervalEnd = 0

    def calculateProbability(self, sumOfTimeNeeded, time1):
        return (self.newJobOption.timeNeeded / sumOfTimeNeeded) * math.pow(math.e, time1)
