from queue_module import *

def readFile(fileName):
    commandFile = open(fileName, "r")
    jobList = []
    for line in commandFile:
        job = line.split()
        jobList = enqueue(jobList, job)
    return jobList

def linearSearch(queue, prop, idx):
    for i in range(len(queue)):
        if queue[i][idx] == prop:
            return i
    return None

def createNewTask(jobList, queue):
    pass

jobList = readFile("MaintenanceScheduler.txt")
queue = []
