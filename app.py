from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask.helpers import flash
import joblib
import numpy as np
import json

model = joblib.load('LGBM.pkl')


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/',methods=['GET','POST'])
def homePage():
    kwargs={'greetings':'I am Up!'}
    return render_template('home.html')
    

@app.route('/predict',methods=['POST'])
def predict():
    result = request.form

    #Applying mean encoding of Experience column
    if result['experience']=='0':
        Work_Experience_enc = 1.552978
    elif result['experience']=='1':
        Work_Experience_enc = 1.563761
    elif result['experience']=='2':
        Work_Experience_enc = 1.564179
    elif result['experience']=='3':
        Work_Experience_enc = 1.588933
    elif result['experience']=='4':
        Work_Experience_enc = 1.649635
    elif result['experience']=='5':
        Work_Experience_enc = 1.544974
    elif result['experience']=='6':
        Work_Experience_enc = 1.558824
    elif result['experience']=='7':
        Work_Experience_enc = 1.520833
    elif result['experience']=='8':
        Work_Experience_enc = 1.622596
    elif result['experience']=='9':
        Work_Experience_enc = 1.536131
    elif result['experience']=='10':
        Work_Experience_enc = 1.800000
    elif result['experience']=='11':
        Work_Experience_enc = 1.522727
    elif result['experience']=='12':
        Work_Experience_enc = 1.214286
    elif result['experience']=='13':
        Work_Experience_enc = 1.567568
    elif result['experience']=='14':
        Work_Experience_enc = 1.536585

    #Applying mean encoding of Profession column
    if result['profession']=='Artist':
        Profession_enc = 1.315586
    elif result['profession']=='Doctor':
        Profession_enc = 1.513081
    elif result['profession']=='Engineer':
        Profession_enc = 1.240343
    elif result['profession']=='Entertainment':
        Profession_enc = 1.224447
    elif result['profession']=='Executive':
        Profession_enc = 1.466227
    elif result['profession']=='Healthcare':
        Profession_enc = 2.493791
    elif result['profession']=='Homemaker':
        Profession_enc = 1.548780
    elif result['profession']=='Lawyer':
        Profession_enc = 1.321086
    elif result['profession']=='Marketing':
        Profession_enc = 2.089041
    
    #Applying mean encoding of Family_Size column
    if result['familysize']=='1':
        Family_Size_enc = 1.242193
    elif result['familysize']=='2':
        Family_Size_enc = 1.383346
    elif result['familysize']=='3':
        Family_Size_enc = 1.702671
    elif result['familysize']=='4':
        Family_Size_enc = 1.799425
    elif result['familysize']=='5':
        Family_Size_enc = 1.913765
    elif result['familysize']=='6':
        Family_Size_enc = 1.933962
    elif result['familysize']=='7':
        Family_Size_enc = 1.750000
    elif result['familysize']=='8':
        Family_Size_enc = 2.120000
    elif result['familysize']=='9':
        Family_Size_enc = 1.818182
    
    #Applying mean encoding of Var_1 column
    if result['category']=='cat_1':
        Var_enc=1.714286
    elif result['category']=='cat_2':
        Var_enc=1.672986
    elif result['category']=='cat_3':
        Var_enc=1.546229
    elif result['category']=='cat_4':
        Var_enc=1.556474
    elif result['category']=='cat_5':
        Var_enc=1.647059
    elif result['category']=='cat_6':
        Var_enc=1.550433
    elif result['category']=='cat_7':
        Var_enc=1.591133

    #Applying Log Transformation of Age column
    Age = np.log10(int(result['age']))

    cols=['Age', 'Work_Experience_enc', 'Profession_enc', 'Family_Size_enc',
       'var_enc', 'Gender_Female', 'Gender_Male', 'Ever_Married_No',
       'Ever_Married_Yes', 'Graduated_No', 'Graduated_Yes',
       'Spending_Score_Average', 'Spending_Score_High', 'Spending_Score_Low']
    enc_input = np.zeros(14)
    enc_input[0]=Age
    enc_input[1]=Work_Experience_enc
    enc_input[2]=Profession_enc
    enc_input[3]=Family_Size_enc
    enc_input[4]=Var_enc
    user_input_Gender = 'Gender_'+result['gender']
    col_Gender = cols.index(user_input_Gender)
    enc_input[col_Gender] = 1
    user_input_Married = 'Ever_Married_'+result['married']
    col_Married = cols.index(user_input_Married)
    enc_input[col_Married] = 1
    user_input_Graduated = 'Graduated_'+result['graduated']
    col_Graduated = cols.index(user_input_Graduated)
    enc_input[col_Graduated] = 1
    user_input_Spending_Score = 'Spending_Score_'+result['spendingscore']
    col_Spending_Score = cols.index(user_input_Spending_Score)
    enc_input[col_Spending_Score] = 1

    print(enc_input)

    pred = model.predict([enc_input])[0]
    
    if pred==0:
        cat = 'A'
    elif pred==1:
        cat = 'B'
    elif pred==2:
        cat = 'C'
    elif pred==3:
        cat = 'D'
    
    print('Output is '+cat)
    return json.dumps({'Segmentation':cat})
    #return redirect(url_for('homePage'))
