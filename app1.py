# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:50:04 2020

@author: Shruti.Vaidya
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])


def predict_note_authentication(Age,Weight,Height,BMI,Blood_Group,Pulse_rate,RR,Hb,Cycle,Cycle_length,Marraige_Status,Pregnant,No_of_aborptions,I_beta_HCG,II_beta_HCG,FSH,LH,FSH_LH_ratio,Hip,Waist,Waist_Hip_Ratio,TSH,AMH,PRL,Vit_D3,PRG,RBS,Weight_gain,hair_growth,Skin_darkening,Hair_loss,Pimples,Fast_food,Reg_Exercise,BP_Systolic,BP_Diastolic,Follicle_No_L,Follicle_No_R,Avg_F_size_L,Avg_F_size_R,Endometrium):
    
    
    l1=[Age,Weight,Height,BMI,Blood_Group,Pulse_rate,RR,Hb,Cycle,Cycle_length,Marraige_Status,Pregnant,No_of_aborptions,I_beta_HCG,II_beta_HCG,FSH,LH,FSH_LH_ratio,Hip,Waist,Waist_Hip_Ratio,TSH,AMH,PRL,Vit_D3,PRG,RBS,Weight_gain,hair_growth,Skin_darkening,Hair_loss,Pimples,Fast_food,Reg_Exercise,BP_Systolic,BP_Diastolic,Follicle_No_L,Follicle_No_R,Avg_F_size_L,Avg_F_size_R,Endometrium]
    arr=np.array([list(map(int, l1))])
    prediction=model.predict(arr)       
    return prediction



def main():
    st.title("PCOS Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit PCOS Prediction ML App </h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    Age  = st.text_input("Age")
    Weight = st.text_input("Weight")
    Height = st.text_input("Height")
    BMI = st.text_input("BMI")
    Blood_Group = st.text_input("Blood_Group[A+=11,1A-=12,B+=13,B-=14,O+=15,O-=16,AB+=17,AB-18]")
    Pulse_rate = st.text_input("Pulse_rate")
    RR = st.text_input("Respiration_Rate")
    Hb = st.text_input("Hb")
    Cycle = st.text_input("Cycle((Enter-2)Regular/(Enter-4)Irregular)")
    Cycle_length = st.text_input("Cycle_length")
    Marraige_Status = st.text_input("Marraige_Status(Yrs)")
    Pregnant = st.text_input("Pregnant[Type-1 for'YES'/0 for'NO']")
    No_of_aborptions = st.text_input("No_of_aborptions")
    I_beta_HCG = st.text_input("I_beta_HCG")
    II_beta_HCG = st.text_input("II_beta_HCG")
    FSH = st.text_input("FSH")
    LH = st.text_input("LH")
    FSH_LH_ratio = st.text_input("FSH_LH_ratio")
    Hip = st.text_input("Hip")
    Waist = st.text_input("Waist")
    Waist_Hip_Ratio = st.text_input("Waist:Hip Ratio")
    TSH  = st.text_input("TSH")
    AMH = st.text_input("AMH")
    PRL = st.text_input("PRL")
    Vit_D3 = st.text_input("Vit D3") 
    PRG = st.text_input("PRG")
    RBS = st.text_input("RBS")
    Weight_gain = st.text_input("Weight_gain[Type-1 for'YES'/0 for'NO']")
    hair_growth = st.text_input("hair_growth[Type-1 for'YES'/0 for'NO']")
    Skin_darkening = st.text_input("Skin_darkening[Type-1 for'YES'/0 for'NO']")
    Hair_loss = st.text_input("Hair_loss[Type-1 for'YES'/0 for'NO']")
    Pimples = st.text_input("Pimples[Type-1 for'YES'/0 for'NO']")
    Fast_food = st.text_input("Fast_food[Type-1 for'YES'/0 for'NO']")
    Reg_Exercise = st.text_input("Reg_Exercise[Type-1 for'YES'/0 for'NO']")
    BP_Systolic = st.text_input("BP_Systolic")
    BP_Diastolic = st.text_input("BP_Diastolic")
    Follicle_No_L= st.text_input("Follicle_No_L")
    Follicle_No_R = st.text_input("Follicle_No_R")
    Avg_F_size_L = st.text_input("Avg_F_size_L") 
    Avg_F_size_R= st.text_input("Avg_F_size_R") 
    Endometrium  = st.text_input("Endometrium")
    result=""
    if st.button("Predict"):
       result=predict_note_authentication(Age,Weight,Height,BMI,Blood_Group,Pulse_rate,RR,Hb,Cycle,Cycle_length,Marraige_Status,Pregnant,No_of_aborptions,I_beta_HCG,II_beta_HCG,FSH,LH,FSH_LH_ratio,Hip,Waist,Waist_Hip_Ratio,TSH,AMH,PRL,Vit_D3,PRG,RBS,Weight_gain,hair_growth,Skin_darkening,Hair_loss,Pimples,Fast_food,Reg_Exercise,BP_Systolic,BP_Diastolic,Follicle_No_L,Follicle_No_R,Avg_F_size_L,Avg_F_size_R,Endometrium)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("[0]==You will not suffer with PCOS/[1]==You will suffer with PCOS")
        st.text("Lets Predict")

if __name__=='__main__':
    main()
    
    
    