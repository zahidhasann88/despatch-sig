from flask import Flask, request, Blueprint, session, flash, redirect, render_template
# from urllib import request
from flask_cors import CORS, cross_origin

from database.dbConnection import database as db
from services import authServices as  auth
from model.DTO.responseDTO import ResponseDTO

app = Blueprint('auth', __name__)
CORS(app)

#written for flask web app

@app.route("/auth/validation-login-info", methods = ['POST', 'GET'])
def get_userFromDB():
    if request.method == 'POST':
        data = request.form
        print(data, "For login")
        flag, user = auth.validation(data)
        print(flag, user, ' printing from validation OKay')
        if not flag:
            # session.pop('_flashes', None)
            session.clear()
            flash('Incorrect Username or Password!')
            return redirect('/')
    session['username'] = user['username']
    session['password'] = user['password']
    session['rank'] = user['type'] #admin/instr/student
    print(session, ' at validation login info')
    # flash('Welcome to SigCen Simulation!')
    return redirect('/auth/home')


@app.route('/auth/home')
def login(data=None):
    if 'username' in session.keys():
        user = db.users.find_one({'username': session['username']})
        if user is not None:
            if user['type'] == 'admin':
                session['rank'] = 'admin'
                print(session)
                return redirect('/admin/home')
            elif user['type'] == 'instr':
                session['rank'] = 'instr'
                return redirect('/instr/home')  # for QC
            elif user['type'] == 'student':
                session['rank'] = 'student'
                # check the type of student account: supt/reg_clerk/acceptance clerk
                return redirect('/student/home')
            else:
                # session.pop('_flashes', None)
                session.clear()
                flash('This user is not Found. Login again or contact to Admin.')
    # else:
    #     session.pop('_flashes', None)
    return render_template('login.html', **locals())


@app.route('/auth/logout')
def logout():
    if 'username' in session.keys():
        session.pop('username')
        session.pop('rank')
        session.pop('password')
    return redirect('/')


@app.route('/auth/cross-access')
def cross_access():
    return render_template('login.html', **locals())


# written for angular js frontend app
@app.route("/get-user-by-username-and-password", methods=['POST', 'GET'])
def get_user_by_username_password():
    # print(request.headers)
    content_type = request.headers.get('Content-Type').__str__().lower()
    if (content_type == 'application/json'):
        json = request.json
        print(json)
        # collection = database["users"]
        #  db.inventory.find( { status: "A", qty: { $lt: 30 } } )
        uname = json["user_name"]  # username found from html form
        pwd = json["user_password"]  # password found from html form
        # user_found = database.users.find( { 'username': uname, 'passwd':  pwd})
        cursor = db.users.find({'username': uname})
        result_user = list(cursor)
        print("USER_FOUND result_user is", result_user)
        if cursor.count()==0 :
            print("user-found is None")
            httpResponse = ResponseDTO("User Not Found", "False", 200, None)
            return httpResponse.__str__()
        else:
            user = result_user[0]
            # print("printing user", user)
            httpResponse = ResponseDTO("User Found", "True", 200, user)
            if user['passwd']!= pwd:
                httpResponse.message = "Username and Password Does Not Match!!"
            else:
                httpResponse.message = "User Login Successful."

            print("PRINTING HTTP RESPONSE:", httpResponse.message, httpResponse)

            return httpResponse.__str__()

    else:
        return 'Content-Type not supported!'


