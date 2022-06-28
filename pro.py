
from flask import Flask, jsonify, request

app=Flask(__name__)
task=[
    {
        "Contact":"6523478017",
        "Name":"task1",        
        "done":False,
        "id":1
    },
        {
        "Contact":"9867575678",
        "Name":"Rahul",
         "done":False,
         "id":2   
    },
   
]
@app.route('/')

def index():
    return"get-data ,||| add-data"

@app.route("/get-data")
def gettask():
    return jsonify({
        "data":task
    })
@app.route("/add-data",methods=["POST"])
def addTask():
    tasknew={       
        "Contact":request.json.get("Contact"),
        #"Name":request.json.get("Name"),
        "done":False,
        "id":task["id"]+2
        }
    task.append(tasknew)
    
if __name__== '__main__':
    app.run()