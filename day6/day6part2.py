import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#generates a list of all documents
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

documents = getDocuments(abs_file_path)

yesPerGroup = list()
workSet = set()
for i in documents:
    #important case, but not used for debugging purposes
    if len(i) == 1:
        for x in i:
            yesPerGroup.append(len(x))
    for x in i[1:]:
        if set(i[0]).intersection(set(x)) == []: #only 1 person in group
            continue
        if len(workSet) == 0: 
            workSet.update(set(i[0]).intersection(set(x)))#first iteration with empty workSet
            if len(workSet) == 0: 
                break
            continue
        workSet = workSet.intersection(set(x)) 
        if len(workSet) == 0:
            break
    yesPerGroup.append(len(workSet))
    workSet.clear()
 
print(sum(yesPerGroup))


