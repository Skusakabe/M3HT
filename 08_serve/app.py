# DWS: David, Wan Ying, Shinji
# SoftDev
# Oct 2022

from flask import Flask
import random as rng
app = Flask(__name__) #create instance of class Flask


def csv_to_dict(file):
    data = file.read()
    result = {}
    lines = data.split("\n") #creates list of all the lines in the csv file
    lines = lines[1:len(lines)-1]

    for oneline in lines:
        if '"' in oneline: #checks for when there is an occupation containing commas
            oneline = oneline[1::] #removes first quotation mark
            values = oneline.split('"') #splits string on second quotation mark, creating a list with the two halves and removes the quotation mark
            values[1] = values[1][1::] #removes the unwanted comma currently part of the string percentage: ",6.1" --> "6.1"values[1] = values[1][1::] #removes the unwanted comma currently part of the string percentage: ",6.1" --> "6.1"
            result[values[0]] = float(values[1]) #adds occupation,percentage pair to dictionary while converting string percentage to float
        else:
            values = oneline.split(",") #splits string on comma, creating a list with the two halves and removes the comma
            result[values[0]] = float(values[1]) #adds occupation,percentage pair to dictionary while converting string percentage to float
    return result

def weighted_random(dnary):
    randval = rng.uniform(0, 100)
    current_val = 0
    if randval >= dnary["Total"]: #to account of the 0.2% not in total
        return "Other"
    for i in dnary.keys():
        if randval >= current_val and randval < current_val + dnary[i]:
            return i
        else:
            current_val += dnary[i]
            
@app.route("/")
def occupation_chooser():
    occ_file = open("occupations.csv", "r")
    a = csv_to_dict(occ_file)
    b = weighted_random(a)
    return "<h1 align = 'center'> DWS: David, Wan Ying, Shinji </h1> </br> </br> </br>" + "<h2 align = 'center'>" + b + "</h2>"

if __name__ == "__main__":
    app.debug = True
    app.run()