import os

#gets map file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#returns True if Tree is there
def isTreeOnPosition(position, line):
    return line[position%len(line)] is '#'

treeCount = 0 
position = 0 #starting at position 0

with open(abs_file_path, "r") as f:
    for line in f:
        if isTreeOnPosition(position, line.strip()):
            treeCount += 1
        position += 3


print(f'Auf dem Weg liegen {treeCount} Bäume!')

#Output Auf dem Weg liegen 78 Bäume!

