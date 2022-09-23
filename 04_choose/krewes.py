import random as rng

krewes1 = {2:["A", "B", "C"], 3:["D", "E", "F"]}
krewes2 = {
    2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"],
    7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
    8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
}
krewes3 = {}

def randdevo(dnary):
    try:
        alldevos = []
        for i in (dnary.keys()):
            alldevos += dnary[i]
        return rng.choice(alldevos)
    except:
        print("Error, dict is length 0")

for i in range(20):
    print(randdevo(krewes2))

def user_picks(dnary):
    choice1 = int(input("Type the number for the period you want to select from. -1 to pick a random period: "))
    while (not(choice1 == 2 or choice1 == 7 or choice1 == 8 or choice1 == -1)):
        print("Invalid value \n")
        choice1 = int(input("Type the number for the period you want to select from. -1 to pick a random period: "))
    choice2 = int(input("How many devos would you like to randomly select? "))
    while (not(choice2 >= 0)):
        print("Invalid value \n")
        choice2 = int(input("How many devos would you like to randomly select? "))
    for i in range(choice2):
        print(randdevo(dnary))
           
user_picks(krewes2)