import random as rng

def generateinfo(times): ## times is the amount of data/people included in the info
    result = ""
    for i in range(times):
        result += str(rng.randint(1,10)) + "$$$"
        for j in range(2):
            for k in range(3):
                result += chr(65 + rng.randint(0,25))
            if (j == 0):
                result += "$$$"
            elif (i < times - 1):
                result += "@@@"
    return result

print(generateinfo(10))

def sortdata(data):
    result = {}
    units = data.split("@@@")
    for i in range(len(units)):
        features = units[i].split("$$$")
        if (features[0] in result.keys()):
            result.update({features[0]: result.get(features[0]) + [[features[1], features[2]]]})
        else:
            result[features[0]] = [[features[1], features[2]]]
    return result
        
print(sortdata(generateinfo(20)))
    