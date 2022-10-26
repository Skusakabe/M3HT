#SJS: Shinji, Jeremy and Sebastian
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

#TODO: figure out how to run the python code multiple times without adding duplicate information into the tables

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS courses(code TEXT, mark INTEGER, id INTEGER)")    
    for row in reader:
        c.execute("INSERT INTO courses values (?, ?, ?)", [row['code'], row['mark'], row['id']])
info = c.execute("select * from courses;").fetchall()
print(info)

# with open('students.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
command = "CREATE TABLE IF NOT EXISTS students(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)"          # test SQL stmt in sqlite3 shell, save as string

c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


