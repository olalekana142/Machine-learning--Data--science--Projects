# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 21:20:43 2021

@author: New Owner
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import base64


st.write(""" 
         # Heart predictive testing App
Heart test is to learn about early heart failure and to be able to prevent it 
seeing it from the early signs """)

df_selected = pd.read_csv('heart_failure_clinical_records_dataset.csv')

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    
    href = f' <a href = "data:file/csv;base64 , {b64}" download = "heart_failure_clinical_records_dataset.csv">Download CSV File</a>'
    return href
st.set_option('deprecation.showPyplotGlobalUse', False)
st.markdown(filedownload(df_selected), unsafe_allow_html=True)

def user_input_features():
    pass
def user_input_features():
    Age = st.sidebar.selectbox('age',('sex'))
    Symptoms =st.sidebar.selectbox('serum_sodium',('smoking','high_blood_pressure', 'diabetes','serum_creatinine'))
    data = {'age':[Age], 'serum_sodium':[Symptoms]}
    
    features = pd.DataFrame(data)
    return features

input_df = user_input_features()


