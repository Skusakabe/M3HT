'''
Shinji Verit
SoftDev
K06 duo mission
2022-09-30
Time spent: 0.8 hours

DISCO:

QCC:
'''

file = open("occupations.csv", "r")
unparsed = file.read()

def csv_to_dict(data):
    result = {}
    lines = data.split("\n")
    lines = lines[1:len(lines)-1]
    for oneline in lines:
        if '"' in oneline:
            oneline = oneline[1::]
            values = oneline.split('"')
#           print(oneline) -> shows that oneline stays unchanged when using oneline.split()
            values[1] = values[1][1::]
            result[values[0]] = float(values[1])
        else:
            values = oneline.split(",")
            result[values[0]] = float(values[1])
    return result

a = csv_to_dict(unparsed)
print(a)