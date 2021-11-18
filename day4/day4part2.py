import os
import re

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#generate tuples
def getTuples(documents):
    tuples = list()
    for tuple in range(len(documents)):
        tuples.append(documents[tuple].partition(':'))
    return tuples

#generates a list of all documents/passports
def getDocuments(abs_file_path):
    with open(abs_file_path, "r") as f:
        f.seek(0)
        documents = list()
        split = list()
        for line in f.readlines(): 
            if line.split() == []:
                documents.append(split) 
                split = []
            split = split + line.split()
        return documents

#checks if 'cid' is in tuple
def hasCidInTuples(tuples):
    for x in range(len(tuples)):
        if tuples[x][0] == 'cid':
            return True
    return False

#checks if document is valid (part1)
# def isValid(tuples):
#     return len(tuples) == 8 or (len(tuples) == 7 and not hasCidInTuples(tuples))

#checks if cid is valid
def isCidValid(tuples):
    return len(tuples) == 8 or (len(tuples) == 7 and not hasCidInTuples(tuples))

#checks if 'tag' is in tuple
def hasTagInTuples(tag, tuples):
    for x in range(len(tuples)):
        if tuples[x][0] == tag:
            return True
    return False

#check if byr is valid
def isValidByr(tuples):
    for x in range(len(tuples)):
        if tuples[x][0] == 'byr':
            if 1920 <= int(tuples[x][2]) <= 2002:
                return True
    return False

#check if iyr is valid
def isValidIyr(tuples):
    for x in range(len(tuples)):
        if tuples[x][0] == 'iyr':
            if 2010 <= int(tuples[x][2]) <= 2020:
                return True
    return False

#check if eyr is valid
def isValidEyr(tuples):
    for x in range(len(tuples)):
        if tuples[x][0] == 'eyr':
            if 2020 <= int(tuples[x][2]) <= 2030:
                return True
    return False

#check if hgt is valid
def isValidHgt(tuples):
    for x in range(len(tuples)):
        if tuples[x][0] == 'hgt':
            number = re.findall('[0-9]+', tuples[x][2])
            letter = re.findall('[ci]', tuples[x][2])
            if not letter:
                return False
            if ((150 <= int(number[0]) <= 193 ) and letter[0] == 'c') or ((59 <= int(number[0]) <= 76) and letter[0] == 'i'):
                return True
    return False

#check if hcl is valid
def isValidHcl(tuples):
    for x in range(len(tuples)):
        if tuples[x][0] == 'hcl':
            if (re.findall('#[0-f][0-f][0-f][0-f][0-f][0-f]', tuples[x][2])):
                return True
    return False

#check if ecl is valid
def isValidEcl(tuples):
    eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for x in range(len(tuples)):
        if tuples[x][0] == 'ecl':
            if tuples[x][2] in eyecolors:
                return True
    return False

#check if pid is valid
def isValidPid(tuples):
    for x in range(len(tuples)):
        if tuples[x][0] == 'pid':
            if (re.findall('^[0-9]{9}$', tuples[x][2])):
                return True
    return False

#check if document is valid
def isValid(tuples):
    return (isValidByr(tuples) and isValidIyr(tuples) and isValidEyr(tuples) and isValidHgt(tuples) and isValidHcl(tuples) and isValidEcl(tuples) and isValidPid(tuples) and isCidValid(tuples))

documents = getDocuments(abs_file_path)
sum = 0
for i in range(len(documents)):
    sum += isValid(getTuples(documents[i]))
print(sum)





