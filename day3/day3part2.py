import os

#gets map file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#returns True if Tree is there
def isTreeOnPosition(position, line):
    return line[position%len(line)] == '#'


def getTreeCount(abs_file_path, rightBy, downBy):
    with open(abs_file_path, "r") as openedFile:
        treeCount = 0
        position = 0
        openedFile.seek(0) # start at line 0 again
        for line in openedFile.readlines()[::downBy]: 
            if isTreeOnPosition(position, line.strip()):
                treeCount += 1
            position += rightBy
        return treeCount


multiplied = \
getTreeCount(abs_file_path, 3, 1) *\
getTreeCount(abs_file_path, 5, 1) *\
getTreeCount(abs_file_path, 7, 1) *\
getTreeCount(abs_file_path, 1, 2) *\
getTreeCount(abs_file_path, 1, 1) 
print(f'Multipliziert ergeben die Bäume {multiplied}.')

#Output: Multipliziert ergeben die Bäume 3064612320.