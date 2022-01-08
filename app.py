from enum import unique
from flask import Flask, render_template, url_for, request
#from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import defaultload

#initialize database instance.
#set the table name to db and app instance to app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///writeup.db'
db = SQLAlchemy(app)


#set column data for table.
class Writups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(120), nullable=False)
    Author = db.Column(db.String(120), nullable=False)
    Date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Description = db.Column(db.Text, nullable=False)

posts = [
    {
        "Title": "Memory Forensics",
        "Author": "Shawn Michael Sudaria",
        "Date_posted": "Oct. 22, 2021", 
        "Description": "We used volatility to analyst the windows memory capture."
    }
]
# Main page content
@app.route("/")
def page():
    message = "Shawn Michael Sudaria"
    return render_template('index.html', msg=message)

@app.route("/CTF", methods=["GET", "POST"])
def CTF():
    return render_template('ctf.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)