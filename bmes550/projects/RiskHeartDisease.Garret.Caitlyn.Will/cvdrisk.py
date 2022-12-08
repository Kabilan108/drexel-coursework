# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:07:50 2022

@author: CocosW, ChristopherC, WhiteG
"""

import streamlit as st
from risk_calc import *
from close_hosp import *
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import scipy.stats as stats
#import math

# Set the title of the GUI
st.title('Cardiovascular Risk')
st.subheader('by Will Cocos, Cait Christopher, Garrett White')

# Overview of the website
st.write("""
        Based on your inputs, this website provides an estimation of 10-year risk of Hard \n
        atherosclerotic cardiovascular disease (ASCVD), which is defined as the first occurrence \n
        of nonfatal myocardial infarction or cornoary heart disease death, or fatal or nonfatal \n
        stroke. The estimation is based on the Pooled Cohort Equations as calculated here \n
        https://www.ahajournals.org/doi/full/10.1161/01.cir.0000437741.48606.98#d1e421
        """)
# This is the user input section
st.subheader('Inputs')

# Sex entry
sex = st.selectbox(
    'What is your biological sex:',
    ('Male', 'Female'))

# Race entry
race = st.selectbox(
    'What is your race:',
    ('White', 'Black or African American', 'American Indian or Alaska Native', 'Asian', 'Native Hawaiian or Other Pacific Islander'))

# Age entry
age = st.number_input(
    "Enter your age (years):",
    value = float(50),
    key="age",
    step = float(1),
    format="%.1f"
    )

# Blood pressure treatment entry
BP_treat = st.selectbox(
    'Are you currently taking medication to control your blood pressure:',
    ('Yes', 'No'))

# Blood pressure entry
BP = st.number_input(
    "Enter your systolic blood pressure (mm Hg):",
    value = float(120),
    key="BP",
    step = float(1),
    format="%.1f"
    )

# Total cholesterol entry
TOT_C = st.number_input(
    "Enter your total cholesterol (mg/dL):",
    value = float(200),
    key="TOT_C",
    step = float(1),
    format="%.1f"
    )

# HDL cholesterol entry
HDL_C = st.number_input(
    "Enter your high-density lipoprotein (HDL) cholesterol (mg/dL):",
    value = float(120),
    key="HDL_C",
    step = float(1),
    format="%.1f"
    )

# Smoker entry
smoker = st.selectbox(
    'Are you currently a smoker:',
    ('Yes', 'No'))

# Diabetes entry
diabetes = st.selectbox(
    'Do you have diabetes:',
    ('Yes', 'No'))

# Zip code entry
zipcode = st.text_input(
    "Enter your zip code (first five digits only):",
    value = "19104",
    key="zipcode"
    )

# This is the user output section
st.subheader('Outputs')

# Output the risk score by calling risk_calc py function
risk = risk_calc(sex, race, age, BP_treat, BP, TOT_C, HDL_C, smoker, diabetes);
st.write("Your 10-year risk of Hard ASCVD is (%): ", risk);

# Output the closest hospital by calling close_hosp py function
close_hosp = close_hosp(zipcode);
st.write("The three closest hospitals to your location are below:");
st.write(close_hosp);