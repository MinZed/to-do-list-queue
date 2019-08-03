from driver import *
 


def readFile(fileName):
    commandFile = open(fileName, "r")
    jobList = []
    for line in commandFile:
        job = line.split()
       jobList.append(job)
    return jobList



def main():
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
        elif command == "modify"
            modify()
