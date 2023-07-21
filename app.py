from flask import Flask, redirect, render_template,  session, flash
from urllib import request
from flask_cors import CORS, cross_origin

from database.dbConnection import database

app = Flask(__name__)
app.secret_key = "ProjGroup2"
CORS(app)

from routes.auth import app as auth_app
app.register_blueprint(auth_app)
from routes.admin.adminRoutes import app as admin_app
app.register_blueprint(admin_app)
from routes.instr.instrRoutes import app as instr_app
app.register_blueprint(instr_app)
from routes.student.studentRoutes import app as student_app
app.register_blueprint(student_app)
@app.route('/')
def hello_world():  # put application's code here
    print(database["users"].find())
    # return redirect("/about-me")
    return redirect("/test-login")

@app.route("/test-login")
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run()

app.run(debug=True)