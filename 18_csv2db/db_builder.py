#SJS: Shinji, Jeremy and Sebastian
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
# with open('courses.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")    
#     for row in reader:
#         c.execute("INSERT INTO courses values (" + "'" + row["code"] + "'" + ", " + row["mark"] + ", " + row["id"] + ")")
c.execute("select * from courses;")

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


