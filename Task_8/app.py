import re
from unittest import result
from flask import Flask, render_template,request

# Create the Object 
app = Flask(__name__)

# Define the Routes and bind it with a Function
@app.route('/',methods=['GET','POST'])
def regex():
    if request.method=='POST':
        input1 = request.form['in1']
        teststring = request.form['test']
        count=0
        if (len(input1) ==0 or len(teststring) == 0):
            count=-1
            return render_template("index.html",result="Please provide input",count=count)
        else:
            lst=[]
            for match in re.finditer(r'{}'.format(input1),teststring):
                string=''
                count+=1
                stn=stn+"Match {} \"{}\" at start and end indices [{} , {}]".format(count,match.group(),match.start(),match.end())
                lst.append(string)
            return render_template("index.html",result ="Matche found", in1=input1, test=teststring, lsts=lst, count=count)

    return render_template("index.html",count=-1)

    
# Run the App
if __name__=='__main__':
    app.run(debug=True)