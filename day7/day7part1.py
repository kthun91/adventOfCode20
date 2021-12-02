import os
import string
from collections import defaultdict

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#generates a list of all rules
def getRules(abs_file_path):
    with open(abs_file_path, "r") as f:
        f.seek(0)
        rules = list()
        for line in f.readlines(): 
            rules.append(line.rstrip(".\n").split(" bags contain "))
        return rules

rules = getRules(abs_file_path)

# def inBagOf(bag, color):
#     for key,value in bag:
#         print(key,value)

bag = defaultdict(dict)
#print(type(bag))
for rule in rules:
    colors = rule[0]
    parts = rule[1].split(", ")
    for id,part in enumerate(parts):
        numberPart = parts[id][0]
        namePart = parts[id][2:].replace(" bags", " bag").replace(" bag", "")
        bag[colors].update({namePart:numberPart})
print(bag["shiny gold"])

for color in bag:
    (bag[color].get('light aqua'))