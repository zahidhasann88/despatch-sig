from flask import Flask, request, Blueprint, session, flash, redirect, render_template
# from urllib import request
from flask_cors import CORS, cross_origin

from database.dbConnection import database as db
from services import authServices, instrServices
from model.DTO.responseDTO import ResponseDTO

app = Blueprint('instr', __name__)
CORS(app)

@app.route('/instr/home', methods=['POST', 'GET'])
# @requires_access_level(ACCESS['instr'])
# admin home page #
def home_page():
    # all_branch_information = return_database()[0]
    flash("Welcome,"+ session['username'] +",  to instr Homepage!")
    return render_template('instr/instrHome.html')




