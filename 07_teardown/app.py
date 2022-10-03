
# your heading here

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. I don't remember where
1. It could be related to the filepath of the app, which is writting in the terminal as
directory/subdirectory/subdirectory/.../appfile
2. In the terminal.
3. It would print whatever __name__ contains
4. No, a value is being returned not printed.
5. Processing had a run method that is continually looped every frame.
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''