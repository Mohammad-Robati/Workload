import math
from workStationJob import WorkStationJob


jobNumbers = int(input())
workStationNumbers = 3
workStation1Jobs = []
workStation2Jobs = []
workStation3Jobs = []
maximumArrivalTime = 0
for i in range(jobNumbers):
    job = input().split()
    if int(job[0]) > maximumArrivalTime:
        maximumArrivalTime = int(job[0])
    workStation1Jobs.append(WorkStationJob(i, int(job[0]), int(job[1])))
    workStation2Jobs.append(WorkStationJob(i, int(job[0]), int(job[2])))
    workStation3Jobs.append(WorkStationJob(i, int(job[0]), int(job[3])))

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
    maximumLength = -1
    thereIsNoAvailable = True
    if (workStation1CurrentEndTime <= workStation2CurrentEndTime) and (
            workStation1CurrentEndTime <= workStation3CurrentEndTime):
        for job in workStation1Jobs:
            if job.checkArrivalState(workStation1CurrentEndTime) and job.checkAvailability(workStation1CurrentEndTime):
                if job.timeNeeded > maximumLength:
                    thereIsNoAvailable = False
                    newJob = job
                    maximumLength = job.timeNeeded
        if thereIsNoAvailable:
            workStation1CurrentEndTime += 1
            continue
        workStation1Jobs.remove(newJob)
        for job in workStation2Jobs:
            if job.jobNumber == newJob.jobNumber:
                if job.limit1Start == -math.inf:
                    job.limit1Start = workStation1CurrentEndTime
                    job.limit1End = workStation1CurrentEndTime + newJob.timeNeeded
                elif job.limit2Start == -math.inf:
                    job.limit2Start = workStation1CurrentEndTime
                    job.limit2End = workStation1CurrentEndTime + newJob.timeNeeded
                else:
                    pass
        for job in workStation3Jobs:
            if job.jobNumber == newJob.jobNumber:
                if job.limit1Start == -math.inf:
                    job.limit1Start = workStation1CurrentEndTime
                    job.limit1End = workStation1CurrentEndTime + newJob.timeNeeded
                elif job.limit2Start == -math.inf:
                    job.limit2Start = workStation1CurrentEndTime
                    job.limit2End = workStation1CurrentEndTime + newJob.timeNeeded
                else:
                    pass
        newJob.startTime = workStation1CurrentEndTime
        workStation1.append(newJob)
        workStation1CurrentEndTime += newJob.timeNeeded
        if len(workStation1Jobs) == 0:
            workStation1TotalEndTime = workStation1CurrentEndTime
            workStation1CurrentEndTime = math.inf
    elif (workStation2CurrentEndTime <= workStation1CurrentEndTime) and (
            workStation2CurrentEndTime <= workStation3CurrentEndTime):
        for job in workStation2Jobs:
            if job.checkArrivalState(workStation2CurrentEndTime) and job.checkAvailability(workStation2CurrentEndTime):
                if job.timeNeeded > maximumLength:
                    thereIsNoAvailable = False
                    newJob = job
                    maximumLength = job.timeNeeded
        if thereIsNoAvailable:
            workStation2CurrentEndTime += 1
            continue
        workStation2Jobs.remove(newJob)
        for job in workStation1Jobs:
            if job.jobNumber == newJob.jobNumber:
                if job.limit1Start == -math.inf:
                    job.limit1Start = workStation2CurrentEndTime
                    job.limit1End = workStation2CurrentEndTime + newJob.timeNeeded
                elif job.limit2Start == -math.inf:
                    job.limit2Start = workStation2CurrentEndTime
                    job.limit2End = workStation2CurrentEndTime + newJob.timeNeeded
                else:
                    pass
        for job in workStation3Jobs:
            if job.jobNumber == newJob.jobNumber:
                if job.limit1Start == -math.inf:
                    job.limit1Start = workStation2CurrentEndTime
                    job.limit1End = workStation2CurrentEndTime + newJob.timeNeeded
                elif job.limit2Start == -math.inf:
                    job.limit2Start = workStation2CurrentEndTime
                    job.limit2End = workStation2CurrentEndTime + newJob.timeNeeded
                else:
                    pass
        newJob.startTime = workStation2CurrentEndTime
        workStation2.append(newJob)
        workStation2CurrentEndTime += newJob.timeNeeded
        if len(workStation2Jobs) == 0:
            workStation2TotalEndTime = workStation2CurrentEndTime
            workStation2CurrentEndTime = math.inf
    elif (workStation3CurrentEndTime <= workStation1CurrentEndTime) and (
            workStation3CurrentEndTime <= workStation2CurrentEndTime):
        for job in workStation3Jobs:
            if job.checkArrivalState(workStation3CurrentEndTime) and job.checkAvailability(workStation3CurrentEndTime):
                if job.timeNeeded > maximumLength:
                    thereIsNoAvailable = False
                    newJob = job
                    maximumLength = job.timeNeeded
        if thereIsNoAvailable:
            workStation3CurrentEndTime += 1
            continue
        workStation3Jobs.remove(newJob)
        for job in workStation1Jobs:
            if job.jobNumber == newJob.jobNumber:
                if job.limit1Start == -math.inf:
                    job.limit1Start = workStation3CurrentEndTime
                    job.limit1End = workStation3CurrentEndTime + newJob.timeNeeded
                elif job.limit2Start == -math.inf:
                    job.limit2Start = workStation3CurrentEndTime
                    job.limit2End = workStation3CurrentEndTime + newJob.timeNeeded
                else:
                    pass
        for job in workStation2Jobs:
            if job.jobNumber == newJob.jobNumber:
                if job.limit1Start == -math.inf:
                    job.limit1Start = workStation3CurrentEndTime
                    job.limit1End = workStation3CurrentEndTime + newJob.timeNeeded
                elif job.limit2Start == -math.inf:
                    job.limit2Start = workStation3CurrentEndTime
                    job.limit2End = workStation3CurrentEndTime + newJob.timeNeeded
                else:
                    pass
        newJob.startTime = workStation3CurrentEndTime
        workStation3.append(newJob)
        workStation3CurrentEndTime += newJob.timeNeeded
        if len(workStation3Jobs) == 0:
            workStation3TotalEndTime = workStation3CurrentEndTime
            workStation3CurrentEndTime = math.inf
print(max(workStation1TotalEndTime, workStation2TotalEndTime, workStation3TotalEndTime))
for i in range(jobNumbers):
    for job in workStation1:
        if job.jobNumber == i:
            print(job.startTime, " ", end='')
            break
    for job in workStation2:
        if job.jobNumber == i:
            print(job.startTime, " ", end='')
            break
    for job in workStation3:
        if job.jobNumber == i:
            print(job.startTime)
            break
