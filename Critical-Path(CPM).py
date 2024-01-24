import numpy as np

class Activity:
    
    def __init__(self, idx, activity, duration) -> None:
        self.idx = idx
        self.activity = activity
        self.duration = duration
        self.predecessor = []
        self.successor = []
        self.early_start = 0
        self.early_finish = 0
        self.late_start = 0
        self.late_finish = 0

file_path = "input2.txt"

activities = {}
index = []

for lines in open(file_path):
     words = lines.rstrip('\n').split(',')
     print(words)
     idx = int(words[0])
     activity = words[1]
     duration = int(words[2])
     predecessors = words[3]

     index.append(idx) #  index list store idx or activity


     activities[idx] = Activity(idx, activity, duration)
#  1 key ---> 1,A,8 value will be in this format

     if (predecessors != ""):
        predecessors = predecessors.split(';')
        for item in predecessors:
            item = int(item)
            # print (str(idx) + " predecessor: " + str(item))
            activities[idx].predecessor.append(item)
            activities[item].successor.append(idx)

# for idx in index:
#     print (idx, activities[idx].predecessor)
#     print (idx, activities[idx].successor)

maxEF = 0

for idx in index:
    if (len(activities[idx].predecessor) == 0):
        activities[idx].early_finish = activities[idx].duration
    else :
        maxTime = 0
        for item in activities[idx].predecessor:# sob gula activity max EF time check korbo
            
                maxTime = max(maxTime,activities[item].early_finish)

        activities[idx].early_start = maxTime # max EF time ta add kore dibo next ES time te
        activities[idx].early_finish = maxTime + activities[idx].duration
    
    print(activities[idx].early_start, activities[idx].early_finish)
    maxEF = max(maxEF, activities[idx].early_finish) # finish line e gia abar MAX EF time check kore store korbo


length = len(index)
for i in range(length):
    idx = index[length-i-1]
    if (len(activities[idx].successor) == 0):
        activities[idx].late_finish = maxEF
        activities[idx].late_start = maxEF - activities[idx].duration
    else :
        minTime = 99999
        for item in activities[idx].successor:
            if (minTime > activities[item].late_start):
                minTime =min ( minTime, activities[item].late_start)
            
        activities[idx].late_finish = minTime
        activities[idx].late_start = minTime - activities[idx].duration
    
    print(activities[idx].early_finish, activities[idx].late_finish)

result = []

for idx in index:
    if (activities[idx].early_finish == activities[idx].late_finish):
        result.append(activities[idx].activity)

for i in range(len(result)-1):    
    print(result[i] + " -> ", end="")

print(result[len(result)-1])
