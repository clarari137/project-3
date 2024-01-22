
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

# # to data filterable
# @app.route("/data-filterable")
# def main_page():
#     ''' Data Table with filters '''
#     return render_template("data-filterable.html")

# # for viz page
# @app.route("/visualization")
# def data_viz():
#     ''' Run data visualization '''
#     return render_template("visualization.html")

# # route to api list page
# @app.route("/api")
# def api_list():
#     """List all available API routes"""
#     return render_template("api.html")

# # route to Team page
# @app.route("/about")
# def about_us():
#     """Team rooster and info"""
#     return render_template("about.html")

# # route to contact info
# @app.route("/contact")
# def contact_us():
#     '''Team contact info'''
#     return render_template("contact.html")

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

# # route to launch date records of 46 years
# @app.route("/api/launch-date")
# def get_all_launch_date():
#     return jsonify(data.get_launch_date())

# # route to metadata - table data description
# @app.route("/api/metadata")
# def get_metadata():
#     return jsonify(data.meta_info())   

# # route to satellite bio data 
# @app.route("/api/satellite-bio")
# def get_all_demoG_data():
#     return jsonify(data.get_satbio_data())

# # filterable by satellite name
# @app.route("/api/satellite-bio/<satellite_name>")
# def get_selected_demoG_data(satellite_name):
#     return jsonify(data.get_satbio_data(satellite_name))

# # route to 46 years satellite launch by country, and counts
# @app.route("/api/lauch-history-by-country")
# def get_all_country_counts():
#     return jsonify(data.get_40yr_sat_lauch_by_country())

# # route to 46 years satellite launch by **chosen** country, and counts
# @app.route("/api/lauch-history-by-country/<country_name>")
# def get_selected_country_counts(country_name):
#     return jsonify(data.get_40yr_sat_lauch_by_country(country_name))

# # master data of 1974-2020 Satellite Info DB
# @app.route("/api/master-record")
# def get_master_recs():
#     return jsonify(data.get_40yr_master_record())


# # top 10 launch year, month, and day counts
# @app.route("/api/top10-launch-dates")
# def get_top10_LaunchDates_recs():
#     return jsonify(data.get_top10_launch_dates())

# # country count per year
# @app.route("/api/countryCountByYear")
# def get_countryCount_Year_Filterable():
#     return jsonify(data.get_countryCount_perYear_perCountry())


# if program is run from this file ::
if __name__ == '__main__':
    app.run(debug=True)


