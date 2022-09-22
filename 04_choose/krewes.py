import random as rng

krewes = {2:[1,2,3], 7:[4,5,6], 8:[7,8,9]}

def randdevo(dnary):
    alldevos = []
    for i in (dnary.keys()):
        alldevos += dnary[i]
    return rng.choice(alldevos)

print(randdevo(krewes))