import time
import math
from workStationJob import WorkStationJob
from main import workLoadAlgorithm

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

workStation1 = []
workStation2 = []
workStation3 = []
answerMinFounded = int(input())
for i in range(jobNumbers):
    answerString = input().split()
    workStation1.append(int(answerString[0]))
    workStation2.append(int(answerString[1]))
    workStation3.append(int(answerString[2]))
answerIsTrue = True
if answerMinFounded > optimalAnswer.maxTimeEnded:
    print("Your answer is more than ours , we can solve it as below in less time: ")
    answerIsTrue = False
    optimalAnswer.printResult(jobNumbers)
else:
    for i in range(jobNumbers):
        if not workStation1JobsPrimary[i].checkArrivalState(workStation1[i]):
            print("job", i + 1, "in WorkStation 1 has entered before its arrival time")
            answerIsTrue = False
        workStation2JobsPrimary[i].limit1Start = workStation1[i]
        workStation2JobsPrimary[i].limit1End = workStation1[i] + workStation1JobsPrimary[i].timeNeeded
        workStation3JobsPrimary[i].limit1Start = workStation1[i]
        workStation3JobsPrimary[i].limit1End = workStation1[i] + workStation1JobsPrimary[i].timeNeeded
        if not workStation2JobsPrimary[i].checkArrivalState(workStation2[i]):
            print("job", i + 1, "in WorkStation 2 has entered before its arrival time")
            answerIsTrue = False
        if not workStation2JobsPrimary[i].checkAvailability(workStation2[i]):
            print("job", i + 1, "has intersection")
            answerIsTrue = False
        workStation3JobsPrimary[i].limit2Start = workStation2[i]
        workStation3JobsPrimary[i].limit2End = workStation2[i] + workStation2JobsPrimary[i].timeNeeded
        if not workStation3JobsPrimary[i].checkArrivalState(workStation3[i]):
            print("job", i + 1, "in WorkStation 3 has entered before its arrival time")
            answerIsTrue = False
        if not workStation3JobsPrimary[i].checkAvailability(workStation3[i]):
            print("job", i + 1, "has intersection")
            answerIsTrue = False
workStation1TimeEnded = 0
workStation2TimeEnded = 0
workStation3TimeEnded = 0
numberOfJobsChosen1 = 0
numberOfJobsChosen2 = 0
numberOfJobsChosen3 = 0
for i in range(jobNumbers):
    minJob = math.inf
    chosenJob = None
    for j in range(jobNumbers):
        if workStation1[j] >= workStation1TimeEnded:
            if workStation1[j] < minJob:
                minJob = workStation1[j]
                chosenJob = j
    if chosenJob is not None:
        numberOfJobsChosen1 += 1
        workStation1TimeEnded = workStation1[chosenJob] + workStation1JobsPrimary[chosenJob].timeNeeded
    else:
        break
for i in range(jobNumbers):
    minJob = math.inf
    chosenJob = None
    for j in range(jobNumbers):
        if workStation2[j] >= workStation2TimeEnded:
            if workStation2[j] < minJob:
                minJob = workStation2[j]
                chosenJob = j
    if chosenJob is not None:
        numberOfJobsChosen2 += 1
        workStation2TimeEnded = workStation2[chosenJob] + workStation2JobsPrimary[chosenJob].timeNeeded
    else:
        break
for i in range(jobNumbers):
    minJob = math.inf
    chosenJob = None
    for j in range(jobNumbers):
        if workStation3[j] >= workStation3TimeEnded:
            if workStation3[j] < minJob:
                minJob = workStation3[j]
                chosenJob = j
    if chosenJob is not None:
        numberOfJobsChosen3 += 1
        workStation3TimeEnded = workStation3[chosenJob] + workStation3JobsPrimary[chosenJob].timeNeeded
    else:
        break
if numberOfJobsChosen1 < jobNumbers:
    print("we have overlap in workStation 1")
    answerIsTrue = False
if numberOfJobsChosen2 < jobNumbers:
    print("we have overlap in workStation 2")
    answerIsTrue = False
if numberOfJobsChosen3 < jobNumbers:
    print("we have overlap in workStation 3")
    answerIsTrue = False
if max(workStation1TimeEnded, workStation2TimeEnded, workStation3TimeEnded) != answerMinFounded:
    print("this answer calculated the total time wrongly!")
    answerIsTrue = False

if answerIsTrue:
    print("Ur answer is True")
else:
    print("Ur answer is False")
