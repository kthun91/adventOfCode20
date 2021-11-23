import os
import string

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
            rules.append(line.rstrip("\n").split(" bags contain "))
        return rules

rules = getRules(abs_file_path)
count = 0
for x in rules:
    count += sum(["shiny gold" in x[1]])
print(count)