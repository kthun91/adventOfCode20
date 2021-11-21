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

#count unique characters of string
def getNumberOfUniqueChars(string):
    return len(set(string))

#concatonate all strings of one group
#count unique chars of string
#sum up
documents = getDocuments(abs_file_path)
sum = 0
for line in documents:
    sum += getNumberOfUniqueChars("".join(line))
print (sum)

# Output
# 6170