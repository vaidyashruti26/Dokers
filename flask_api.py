# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:50:04 2020

@author: shruti.vaidya
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    Age  = request.args.get("Age")
    Weight = request.args.get("Weight")
    Height = request.args.get("Height")
    BMI = request.args.get("BMI")
    Blood_Group = request.args.get("Blood_Group")
    Pulse_rate = request.args.get("Pulse_rate")
    RR = request.args.get("RR")
    Hb = request.args.get("Hb")
    Cycle = request.args.get("Cycle")
    Cycle_length =request.args.get("Cycle_length")
    Marraige_Status =request.args.get("Marraige_Status")
    Pregnant = request.args.get("Pregnant")
    No_of_aborptions = request.args.get("No_of_aborptions")
    I_beta_HCG = request.args.get("I_beta_HCG")
    II_beta_HCG = request.args.get("II_beta_HCG")
    FSH = request.args.get("FSH")
    LH =request.args.get("LH")
    FSH_LH_ratio = request.args.get("FSH_LH_ratio")
    Hip = request.args.get("Hip")
    Waist = request.args.get("Waist")
    Waist_Hip_Ratio = request.args.get("Waist_Hip_Ratio")
    TSH  =request.args.get("TSH")
    AMH = request.args.get("AMH")
    PRL = request.args.get("PRL")
    Vit_D3 = request.args.get("Vit_D3") 
    PRG = request.args.get("PRG")
    RBS = request.args.get("RBS")
    Weight_gain = request.args.get("Weight_gain")
    hair_growth = request.args.get("hair_growth")
    Skin_darkening = request.args.get("Skin_darkening")
    Hair_loss = request.args.get("Hair_loss")
    Pimples = request.args.get("Pimples")
    Fast_food = request.args.get("Fast_food")
    Reg_Exercise = request.args.get("Reg_Exercise")
    BP_Systolic = request.args.get("BP_Systolic")
    BP_Diastolic = request.args.get("BP_Diastolic")
    Follicle_No_L= request.args.get("Follicle_No_L")
    Follicle_No_R = request.args.get("Follicle_No_R")
    Avg_F_size_L = request.args.get("Avg_F_size_L") 
    Avg_F_size_R= request.args.get("Avg_F_size_R") 
    Endometrium  = request.args.get("Endometrium")
 
    l1=[Age,Weight,Height,BMI,Blood_Group,Pulse_rate,RR,Hb,Cycle,Cycle_length,Marraige_Status,Pregnant,No_of_aborptions,I_beta_HCG,II_beta_HCG,FSH,LH,FSH_LH_ratio,Hip,Waist,Waist_Hip_Ratio,TSH,AMH,PRL,Vit_D3,PRG,RBS,Weight_gain,hair_growth,Skin_darkening,Hair_loss,Pimples,Fast_food,Reg_Exercise,BP_Systolic,BP_Diastolic,Follicle_No_L,Follicle_No_R,Avg_F_size_L,Avg_F_size_R,Endometrium]
    arr=np.array([list(map(int, l1))])
    prediction=model.predict(arr)  
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
   
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=model.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
    