import os
import re #regular epressions

#generate string tuple
def getStringTuple(string):
    return string.partition(': ')

#counts specific chars in string
def numberOfCharInString(string, char):
    return string.count(char)

#gets password string
def getPassword(tuple):
    return tuple[2]

#gets char to look after
def charToCheck(tuple):
    return "".join(re.split("[^a-z]",tuple[0]))

#gets only numbers and minus as string
def getStringOfIntervall(tuple):
    return "".join(re.findall("[0-9]*[-][0-9]*",tuple[0]))

#gets first number of intervall
def getFirstIntervallNumber(string):
    numberTuple = "".join(re.findall("[0-9]*[-][0-9]*",string)).partition('-')
    return numberTuple[0]

#gets second number of intervall
def getSecondIntervallNumber(string):
    numberTuple = "".join(re.findall("[0-9]*[-][0-9]*",string)).partition('-')
    return numberTuple[2]

#check if password is valid
def passwordIsValid(beginIntervall, endIntervall, password, char):
    return int(beginIntervall) <= numberOfCharInString(password, char) <= int(endIntervall)

#gets password file on every system
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "passwords.txt"
abs_file_path = os.path.join(script_dir, rel_path)

numberOfValidPasswords = 0

f = open(abs_file_path, "r") #opens file
for line in f:
    stringtuple = getStringTuple(line.strip())
    password = getPassword(stringtuple)
    char = charToCheck(stringtuple)
    numberString = getStringOfIntervall(stringtuple)
    first = getFirstIntervallNumber(numberString)
    second = getSecondIntervallNumber(numberString)
    
    if passwordIsValid(first, second, password, char):
        numberOfValidPasswords += 1
f.close #closes file

print(numberOfValidPasswords)