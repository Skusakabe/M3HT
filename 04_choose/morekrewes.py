import random as rng

'''
Shinji Verit
SoftDev
K05 duo mission
2022-09-28
Time spent: 0.2 hours

DISCO:
Parse parts of strings into a list using split(separator) method
When adding a list to a list, you can put the list you're adding in [] to add the list that has all of the values
as a single element rather than having an element for all of the values in the list seperately.

QCC:

'''

def generate_info(times): ## times is the amount of data/people included in the info
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

def sort_data(data):
    result = {}
    units = data.split("@@@")
    for i in range(len(units)):
        features = units[i].split("$$$")
        if (features[0] in result.keys()):
            result.update({features[0]: result.get(features[0]) + [[features[1], features[2]]]})
        else:
            result[features[0]] = [[features[1], features[2]]]
    return result
        
test1 = sort_data(generate_info(20))

def rand_devo(dnary):
    try:
        alldevos = []
        for i in (dnary.keys()):
            thisperiod = dnary[i]
            for j in (thisperiod):
                j.append(i)
                alldevos += [j]
        randompick = rng.choice(alldevos)
        print("Name: " + randompick[0] + " Period: " + randompick[2] + " Ducky name: " + randompick[1])
    except:
        print("Error, dict is length 0")
        
print(test1)
print("\n")
rand_devo(test1)