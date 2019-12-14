class Answer:
    def __init__(self, maxTimeEnded, workStation1, workStation2, workStation3, jobNumbers):
        self.maxTimeEnded = maxTimeEnded
        self.workStation1 = workStation1
        self.workStation2 = workStation2
        self.workStation3 = workStation3
        self.jobNumbers = jobNumbers

    def printResult(self):
        print(self.maxTimeEnded)
        for j in range(self.jobNumbers):
            for job in self.workStation1:
                if job.jobNumber == j:
                    print(job.startTime, " ", end='')
                    self.workStation1.remove(job)
                    break
            for job in self.workStation2:
                if job.jobNumber == j:
                    print(job.startTime, " ", end='')
                    self.workStation2.remove(job)
                    break
            for job in self.workStation3:
                if job.jobNumber == j:
                    print(job.startTime)
                    self.workStation3.remove(job)
                    break