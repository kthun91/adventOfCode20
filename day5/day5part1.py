import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def getLowerHalf(rowList):
    if len(rowList) == 1:
        return rowList
    return list(range(rowList[0],rowList[0]+int(len(rowList)/2)))

def getHigherHalf(rowList):
    if len(rowList) == 1:
        return rowList
    return list(range(rowList[0-int(len(rowList)/2)], rowList[-1]+1))

def checkSeatIdLength(abs_file_path):
    with open(abs_file_path, "r") as f:
        for line in f.readlines():
            if (len(line.split())) != 1:
                print("Invalid ID found!")

def getRowNumber(rowList, inputString):
    for char in inputString:
        if char == 'B':
            rowList = getHigherHalf(rowList)
        if char == 'F':
            rowList = getLowerHalf(rowList)
    return rowList

def getColumnNumber(columnList, inputString):
    for char in inputString:
        if char == 'R':
            columnList = getHigherHalf(columnList)
        if char == 'L':
            columnList = getLowerHalf(columnList)
    return columnList

def puzzleSolution(rowNumber, columnNumber):
    return rowNumber[0] * 8 + columnNumber[0]

rows = list(range(0,128))
columns = list(range(0,8))

# 1. read seat-ID
# 2. code to number
# 3. append to solution list
# 4. sort list
with open(abs_file_path, "r") as f:
    solutionList = list()
    for line in f.readlines():
        solutionList.append(puzzleSolution(getRowNumber(rows, line), getColumnNumber(columns, line)))
    solutionList.sort()
    print(solutionList)

