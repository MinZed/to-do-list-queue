from queue_module import *
from datetime import datetime
import time



def linearSearch(queue, idx):
    allElements = []
    for i in range(size(queue)):
        allElements.append(queue[i][idx])
    return allElements




def linearSearch2(queue, idx):
    allElements = []
    for i in range(size(queue)):
        allElements.append(queue[i][idx])
    return allElements


def createNewTask(rawJob, queue):
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







def active(queue):    
    if queue == None:
        print("No Jobs Available")
    else:
        totalNum = 0
        totalPr = 0
        for i in range (len(queue)):
            totalPr += queue[i][1]
            totalNum += 1
        print("Total Number of jobs: " + str(totalNum) + " Average priority: " + str(totalPr/totalNum))

    

def modify(queue, jobNum, job):
    for i in range (len(queue)):
        if queue[i][0] == jobNum:
            queue[i] = job

            print("Modified job " + str(jobNum))
        else:
            print("The job details cannot be modified.")


def remove(queue, jobNum):
    for i in range(len(queue)):
        if queue[i][0] == jobNum:
            queue[i], queue[0] = queue[0], queue[i]
            dequeue(queue)
    return queue



def details(queue, jobNum):
    for i in range(len(queue)):
        if queue[i][0] == jobNum:
            print(queue[i])


def statistics(queue):
    maintenance = 0
    cleaning = 0
    carpentry = 0
    
    for i in range(len(queue)):
        if queue[i][2] == "maintenance":
            maintenance += 1
        elif queue[i][2] == "carpentry":
            carpentry += 1
        elif queue[i][2] == "cleaning":
            cleaning += 1
        else:
            print( "job number" + queue[i][0] + "type error.")


def nextJob(queue):
    nextJ = look(queue)
    if nextJ != None:
        print("Next job is: " + nextJ[0] +
                  ". Job priority is: " + nextJ[1] +
                      ". Job type is: " + nextJ[2])
    else:
        print("No jobs remaining.")


def sleep(second):
    time.sleep(second)











        
            
