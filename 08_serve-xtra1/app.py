# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument? Simplest, most concise answer best.

if __name__ == "__main__":
    app.debug = True
    app.run()

'''
Q0: When the file is run, it wouldnt use the template. Actually doesn't run because of a name error, as the render_template doesn't exist
anymore.
Q1: 1.27.0.0:5000/my_foist_template
Q2: The first argument says which template to use, second one changes foo title to fooooo, third sets the collection being iterated.

'''