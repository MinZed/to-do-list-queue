from queue_module import *
from datetime import datetime

def readFile(fileName):
    commandFile = open(fileName, "r")
    jobList = []
    for line in commandFile:
        job = line.split()
        jobList.append(job)
    return jobList

def linearSearch(queue, idx):
    allElements = []
    for i in range(size(queue)):
        allElements.append(queue[i][idx])
    return allElements

def createNewTask(rawJob, queue):
    # ['received', '205', '14', 'maintenance']
    # will use: ID, timestamp, priority, type
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    job = [int(j) if j.isdigit() else j for j in rawJob[1:]]
    job.insert(1, timestamp)
    if job[2] >= 30:
        job[2] == 30
    if job[2] <= 1:
        job[2] == 1
    newQueue = enqueue(queue, job)
    print(f"Adding job {job[0]} to the queue with timestamp {job[1]}. The priority of the job is {job[2]}. The job type is {job[3]}")
    return newQueue

def respond(queue):
    nextJob = look(queue)
    if nextJob is not None:
        now = datetime.now()
        jobTimestamp = datetime.fromtimestamp(nextJob[1])
        diff = now - jobTimestamp
        print(f"Completed job {nextJob[0]} in {diff.total_seconds()} seconds")
        return
    print("No current tasks — time for a coffee break!")

def activeJobs(queue):
    numOfJobs = size(queue)
    if numOfJobs <= 0:
        print("No Jobs Available")
        return
    avg = sum(linearSearch(queue, 2)) / numOfJobs
    print(f"Total Number of jobs: {numOfJobs} Average priority: {avg}")

jobList = readFile("MaintenanceScheduler.txt")
queue = []
for j in jobList:
    command = j[0].lower()
    if command == "received":
        queue = createNewTask(j)
    elif command == "respond":
        respond(queue)
    elif command == "active":
        activeJobs(queue)
