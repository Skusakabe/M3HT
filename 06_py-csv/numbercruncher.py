file = open("occupations.csv", "r")
unparsed = file.read()

def csv_to_dict(data):
    result = {}
    lines = data.split("\n")
    for oneline in lines:
        if '"' in oneline:
            oneline = oneline[1::]
            values = oneline.split('"')
#           print(oneline) -> shows that oneline stays unchanged when using oneline.split()
            values[1] = values[1][1::]
            print(values)
        else:
            values = oneline.split(",")

csv_to_dict(unparsed)