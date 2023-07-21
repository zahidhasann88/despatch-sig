from flask import Flask, request, Blueprint, session, flash, redirect, render_template
# from urllib import request
from flask_cors import CORS, cross_origin

from database.dbConnection import database as db
from services import authServices, adminServices
from model.DTO.responseDTO import ResponseDTO

app = Blueprint('admin', __name__)
CORS(app)

@app.route('/admin/home', methods=['POST', 'GET'])
# @requires_access_level(ACCESS['admin'])
# admin home page #
def home_page():
    # all_branch_information = return_database()[0]
    all_userList,_ = adminServices.fetch_all_users_from_db()
    # return render_template('Admin/admin_homepage.html', branch_information=all_branch_information)
    return render_template('Admin/adminHome.html', all_users=all_userList)




