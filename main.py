import math
import random
import time
import copy
from workStationJob import WorkStationJob
from answer import Answer
from simulatedAnnealing import SimulatedAnnealing


def workLoadAlgorithm(workStation1JobsPrimary, workStation2JobsPrimary, workStation3JobsPrimary, answers):
    time1 = -0.05
    timeStep = -0.01
    workStation1Jobs = copy.deepcopy(workStation1JobsPrimary)
    workStation2Jobs = copy.deepcopy(workStation2JobsPrimary)
    workStation3Jobs = copy.deepcopy(workStation3JobsPrimary)
    workStation1 = []
    workStation2 = []
    workStation3 = []
    workStation1CurrentEndTime = 0
    workStation2CurrentEndTime = 0
    workStation3CurrentEndTime = 0
    workStation1TotalEndTime = 0
    workStation2TotalEndTime = 0
    workStation3TotalEndTime = 0
    while len(workStation1Jobs) != 0 or len(workStation2Jobs) != 0 or len(workStation3Jobs) != 0:
        newJob = None
        newJobOptions = []
        sumOfTimeNeeded = 0
        probabilityIntervalStart = 0
        time1 += timeStep
        thereIsNoAvailable = True
        if (workStation1CurrentEndTime <= workStation2CurrentEndTime) and (
                workStation1CurrentEndTime <= workStation3CurrentEndTime):
            for job in workStation1Jobs:
                if job.checkArrivalState(workStation1CurrentEndTime) and job.checkAvailability(
                        workStation1CurrentEndTime):
                    thereIsNoAvailable = False
                    newJobOptions.append(SimulatedAnnealing(job))
                    sumOfTimeNeeded += job.timeNeeded

            if thereIsNoAvailable:
                workStation1CurrentEndTime += 1
                continue

            for jobOption in newJobOptions:
                jobOption.probabilityIntervalStart = probabilityIntervalStart
                jobOption.probabilityIntervalEnd = probabilityIntervalStart + jobOption.calculateProbability(
                    sumOfTimeNeeded, time1)
                probabilityIntervalStart = jobOption.probabilityIntervalEnd
            randomNumber = random.uniform(0, probabilityIntervalStart)
            for jobOption in newJobOptions:
                if jobOption.probabilityIntervalStart <= randomNumber < jobOption.probabilityIntervalEnd:
                    newJob = jobOption.newJobOption
                    break

            for job in workStation2Jobs:
                if job.jobNumber == newJob.jobNumber:
                    if job.limit1Start == 0 and job.limit1End == 0:
                        job.limit1Start = workStation1CurrentEndTime
                        job.limit1End = workStation1CurrentEndTime + newJob.timeNeeded
                    elif job.limit2Start == 0 and job.limit2End == 0:
                        job.limit2Start = workStation1CurrentEndTime
                        job.limit2End = workStation1CurrentEndTime + newJob.timeNeeded
                    else:
                        pass
                    break

            for job in workStation3Jobs:
                if job.jobNumber == newJob.jobNumber:
                    if job.limit1Start == 0 and job.limit1End == 0:
                        job.limit1Start = workStation1CurrentEndTime
                        job.limit1End = workStation1CurrentEndTime + newJob.timeNeeded
                    elif job.limit2Start == 0 and job.limit2End == 0:
                        job.limit2Start = workStation1CurrentEndTime
                        job.limit2End = workStation1CurrentEndTime + newJob.timeNeeded
                    else:
                        pass
                    break
            newJob.startTime = workStation1CurrentEndTime
            workStation1.append(newJob)
            workStation1CurrentEndTime += newJob.timeNeeded
            workStation1Jobs.remove(newJob)
            if len(workStation1Jobs) == 0:
                workStation1TotalEndTime = workStation1CurrentEndTime
                workStation1CurrentEndTime = math.inf
        elif (workStation2CurrentEndTime <= workStation1CurrentEndTime) and (
                workStation2CurrentEndTime <= workStation3CurrentEndTime):
            for job in workStation2Jobs:
                if job.checkArrivalState(workStation2CurrentEndTime) and job.checkAvailability(
                        workStation2CurrentEndTime):
                    thereIsNoAvailable = False
                    newJobOptions.append(SimulatedAnnealing(job))
                    sumOfTimeNeeded += job.timeNeeded

            if thereIsNoAvailable:
                workStation2CurrentEndTime += 1
                continue

            for jobOption in newJobOptions:
                jobOption.probabilityIntervalStart = probabilityIntervalStart
                jobOption.probabilityIntervalEnd = probabilityIntervalStart + jobOption.calculateProbability(
                    sumOfTimeNeeded, time1)
                probabilityIntervalStart = jobOption.probabilityIntervalEnd
            randomNumber = random.uniform(0, probabilityIntervalStart)
            for jobOption in newJobOptions:
                if jobOption.probabilityIntervalStart <= randomNumber < jobOption.probabilityIntervalEnd:
                    newJob = jobOption.newJobOption
                    break

            workStation2Jobs.remove(newJob)
            for job in workStation1Jobs:
                if job.jobNumber == newJob.jobNumber:
                    if job.limit1Start == 0 and job.limit1End == 0:
                        job.limit1Start = workStation2CurrentEndTime
                        job.limit1End = workStation2CurrentEndTime + newJob.timeNeeded
                    elif job.limit2Start == 0 and job.limit2End == 0:
                        job.limit2Start = workStation2CurrentEndTime
                        job.limit2End = workStation2CurrentEndTime + newJob.timeNeeded
                    else:
                        pass
                    break

            for job in workStation3Jobs:
                if job.jobNumber == newJob.jobNumber:
                    if job.limit1Start == 0 and job.limit1End == 0:
                        job.limit1Start = workStation2CurrentEndTime
                        job.limit1End = workStation2CurrentEndTime + newJob.timeNeeded
                    elif job.limit2Start == 0 and job.limit2End == 0:
                        job.limit2Start = workStation2CurrentEndTime
                        job.limit2End = workStation2CurrentEndTime + newJob.timeNeeded
                    else:
                        pass
                    break
            newJob.startTime = workStation2CurrentEndTime
            workStation2.append(newJob)
            workStation2CurrentEndTime += newJob.timeNeeded
            if len(workStation2Jobs) == 0:
                workStation2TotalEndTime = workStation2CurrentEndTime
                workStation2CurrentEndTime = math.inf
        elif (workStation3CurrentEndTime <= workStation1CurrentEndTime) and (
                workStation3CurrentEndTime <= workStation2CurrentEndTime):
            for job in workStation3Jobs:
                if job.checkArrivalState(workStation3CurrentEndTime) and job.checkAvailability(
                        workStation3CurrentEndTime):
                    thereIsNoAvailable = False
                    newJobOptions.append(SimulatedAnnealing(job))
                    sumOfTimeNeeded += job.timeNeeded

            if thereIsNoAvailable:
                workStation3CurrentEndTime += 1
                continue

            for jobOption in newJobOptions:
                jobOption.probabilityIntervalStart = probabilityIntervalStart
                jobOption.probabilityIntervalEnd = probabilityIntervalStart + jobOption.calculateProbability(
                    sumOfTimeNeeded, time1)
                probabilityIntervalStart = jobOption.probabilityIntervalEnd
            randomNumber = random.uniform(0, probabilityIntervalStart)
            for jobOption in newJobOptions:
                if jobOption.probabilityIntervalStart <= randomNumber < jobOption.probabilityIntervalEnd:
                    newJob = jobOption.newJobOption
                    break

            workStation3Jobs.remove(newJob)
            for job in workStation1Jobs:
                if job.jobNumber == newJob.jobNumber:
                    if job.limit1Start == 0 and job.limit1End == 0:
                        job.limit1Start = workStation3CurrentEndTime
                        job.limit1End = workStation3CurrentEndTime + newJob.timeNeeded
                    elif job.limit2Start == 0 and job.limit2End == 0:
                        job.limit2Start = workStation3CurrentEndTime
                        job.limit2End = workStation3CurrentEndTime + newJob.timeNeeded
                    else:
                        pass
                    break
            for job in workStation2Jobs:
                if job.jobNumber == newJob.jobNumber:
                    if job.limit1Start == 0 and job.limit1End == 0:
                        job.limit1Start = workStation3CurrentEndTime
                        job.limit1End = workStation3CurrentEndTime + newJob.timeNeeded
                    elif job.limit2Start == 0 and job.limit2End == 0:
                        job.limit2Start = workStation3CurrentEndTime
                        job.limit2End = workStation3CurrentEndTime + newJob.timeNeeded
                    else:
                        pass
                    break
            newJob.startTime = workStation3CurrentEndTime
            workStation3.append(newJob)
            workStation3CurrentEndTime += newJob.timeNeeded
            if len(workStation3Jobs) == 0:
                workStation3TotalEndTime = workStation3CurrentEndTime
                workStation3CurrentEndTime = math.inf
    newAnswer = Answer(max(workStation1TotalEndTime, workStation2TotalEndTime, workStation3TotalEndTime),
                       workStation1, workStation2, workStation3)
    answers.append(newAnswer)


if __name__ == "__main__":
    jobNumbers = int(input())
    workStation1JobsPrimary = []
    workStation2JobsPrimary = []
    workStation3JobsPrimary = []
    answers = []
    for i in range(jobNumbers):
        jobString = input().split()
        workStation1JobsPrimary.append(WorkStationJob(i, int(jobString[0]), int(jobString[1])))
        workStation2JobsPrimary.append(WorkStationJob(i, int(jobString[0]), int(jobString[2])))
        workStation3JobsPrimary.append(WorkStationJob(i, int(jobString[0]), int(jobString[3])))
    beginTime = time.process_time()
    while time.process_time() - beginTime < 10.0:
        workLoadAlgorithm(workStation1JobsPrimary, workStation2JobsPrimary, workStation3JobsPrimary, answers)
    minAnswer = math.inf
    optimalAnswer = None
    for answer in answers:
        if answer.maxTimeEnded <= minAnswer:
            optimalAnswer = answer
            minAnswer = answer.maxTimeEnded
    optimalAnswer.printResult(jobNumbers)