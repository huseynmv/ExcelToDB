import sqlite3
from flask.templating import render_template_string
import pandas as pd
from sqlalchemy import create_engine, engine
from flask import Flask,render_template,request,redirect
import os
from werkzeug.utils import secure_filename
app=Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# file = 'pragmatech.xlsx'
# output = 'output.xlsx'



# df = pd.read_excel(file, sheet_name='Sheet1')
# df

# df = pd.read_excel('pragmatech.xlsx')
# print(df.head())

# engine = create_engine("sqlite:///data.db", echo=False)

@app.route("/salam")
def salam():
    return render_template("salam.html")
@app.route("/", methods=["GET","POST"])
def func():
    if request.method=="POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/')
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)



