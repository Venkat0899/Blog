
import pymongo
from flask import Flask, render_template,request
import datetime
app=Flask(__name__)

#client=MongoClient("mongodb+srv://venkat2:chinta@cluster0.wqjeeoj.mongodb.net/?retryWrites=true&w=majority")
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client['flask']
mycol = db["entriestable"]
@app.route('/',methods=["GET","POST"])
def home():
    if request.method =="POST":
        f_content=request.form.get("content")
        
        f_date=datetime.datetime.today().strftime("%y-%m-%d")
        mycol.insert_one({"content":f_content,"p_date":f_date})
    entries_with_date=[
        (
        entry["content"],
        entry["p_date"],
        datetime.datetime.strptime(entry["p_date"],"%y-%m-%d").strftime("%b %d")
        )
        for entry in mycol.find()
    ]
   
    return render_template("index.html" , entries=entries_with_date)


    