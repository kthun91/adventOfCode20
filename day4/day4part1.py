import os

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

#checks if document is valid
def isValid(tuples):
    return len(tuples) == 8 or (len(tuples) == 7 and not hasCidInTuples(tuples))
    
documents = getDocuments(abs_file_path)
sum = 0
for i in range(len(documents)):
    sum += isValid(getTuples(documents[i]))
print(sum)

#Output 206










