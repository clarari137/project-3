
# Author: Henry Le
# Date: Jun. 15, 2020
# version 0 - first release
# if you some how find this file of mine on github, please feel free to take and modify it. I wish you the best of luck on what you want to do.
# learning coding is not easy as it's about learning a new language!

# dependencies
from  WalkabilityData import Walkability 
from flask import Flask, jsonify, render_template, send_file
import io
import base64
import numpy as np
# import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData, Table, func
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import pandas as pd



################### DB Connection #################
data = Walkability("sqlite:///WalkabilitySubset.db")

################## Flask App set up###############
app = Flask(__name__)

####### custome routes for website and data######
# main home page route
@app.route("/")
def home_page():
    ''' Home Page Access Route'''
    return render_template("index.html")

# route to walkability index
@app.route("/api/walkability-directory")
def get_all_walkability_name():
    return jsonify(data.get_walkability_name())

@app.route("/api/full-data")
def get_all_full_data():
    return jsonify(data.get_full_data())

@app.route("/api/demo-data")
def get_demo_data():
    return jsonify(data.demo_data())

@app.route("/api/pie-data")
def get_all_pie_data():
    return jsonify(data.get_pie_data())


# if program is run from this file ::
if __name__ == '__main__':
    app.run(debug=True)


