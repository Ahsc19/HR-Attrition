#imports
import streamlit as st
import streamlit.components.v1 as components
import pydeck as pdk
import numpy as np
import pandas as pd 
from functools import reduce
import altair as alt
import matplotlib as plt


#Config
alt.renderers.set_embed_options(theme='dark')

# page config

st.set_page_config(page_title='HR dashboard',
                    page_icon="",
                    layout='wide'
)

#Importing the dataset and starting EDA

@st.experimental_singleton
def load_data():
    manager_survey = pd.read_csv('manager_survey_data.csv',  sep = ',')
    return manager_survey

manager_survey = load_data()

@st.experimental_singleton
def load_data():
    general_data = pd.read_csv('general_data.csv',  sep = ',')
    return general_data

general_data = load_data()

@st.experimental_singleton
def load_data():
    employee_data = pd.read_csv('employee_survey_data.csv',  sep = ',')
    return employee_data

employee_data = load_data()

emp_man = pd.merge(manager_survey, employee_data, on='EmployeeID')
data_hr = pd.merge(emp_man, general_data, on='EmployeeID')

data_hr.dropna(inplace=True)
data_hr.drop(['Over18', 'EmployeeCount', 'StandardHours'], inplace=True, axis=1)

data_hr = data_hr.astype({'EnvironmentSatisfaction':'int64','JobSatisfaction':'int64','WorkLifeBalance':'int64','NumCompaniesWorked':'int64'})
data_hr['Attrition'] = data_hr['Attrition'].replace(['Yes'],True)
data_hr['Attrition'] = data_hr['Attrition'].replace(['No'],False)

#Interface


st.title("HR Data Set - Module 1")

from PIL import Image
image = Image.open('HR.png')

st.image(image)

st.subheader("This is the front page for the HR data dashboard!")

st.text("This dashboard is based on the HR dataset which contains information from 4300 employees.")
st.text("On the side of the dashboard you can gain more information about this company by clicking on 'Department-Overview'.")
st.text("To see our Supervised Machine Learning model, click on 'Prediction-of-Attrition'.")


labels = 'Female', 'Male'
female_size = AttritionFalse[AttritionFalse.Gender == 'Female'].value_counts().sum()
male_size = AttritionFalse[AttritionFalse.Gender == 'Male'].value_counts().sum()
sizes = [female_size, male_size]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')

st.pyplot(fig1)