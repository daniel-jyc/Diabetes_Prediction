import pandas as pd
import numpy as np
import pickle
import streamlit as st
import lightgbm

#Code to run file
#streamlit run app.py

st.title('Diabetes Risk Prediction :candy:')

HighBP = st.radio('Do you have high blood pressure',['Yes','No'])
HighBP = 1.0 if HighBP == 'Yes' else 0.0

HighChol = st.radio('High Cholesterol',['Yes','No'])
HighChol = 1.0 if HighChol == 'Yes' else 0.0

CholCheck = st.radio('Have you checked cholesterol in past five years?',['Yes','No'])
CholCheck = 1.0 if CholCheck == 'Yes' else 0.0
## weight height conversion??
BMI = st.slider('BMI',0,100)
BMI = float(BMI)

Smoker = st.radio('Have you smoked at least 100 cigarettes in your entire life?',['Yes','No'])
Smoker = 1.0 if Smoker == 'Yes' else 0.0

Stroke = st.radio('Have you ever had a stroke',['Yes','No'])
Stroke = 1.0 if Stroke == 'Yes' else 0.0

HeartDiseaseorAttack = st.radio('Do you have coronary heart disease or myocardinal infarction?',['Yes','No'])
HeartDiseaseorAttack = 1.0 if HeartDiseaseorAttack == 'Yes' else 0.0

PhysActivity = st.radio('Have you done any physical activity in past 30 days?',['Yes','No'])
PhysActivity = 1.0 if PhysActivity == 'Yes' else 0.0

Fruits = st.radio('Do you consume fruit 1 or more times per day?',['Yes','No'])
Fruits = 1.0 if Fruits == 'Yes' else 0.0

Veggies = st.radio('Do you consume vegetables 1 or more times per day?',['Yes','No'])
Veggies = 1.0 if Veggies == 'Yes' else 0.0

HvyAlcoholConsump = st.radio('Do you have more than 14 drinks per week (male) or 7 drinks per week (female)',['Yes','No'])
HvyAlcoholConsump = 1.0 if HvyAlcoholConsump == 'Yes' else 0.0

AnyHealthcare = st.radio('Do you have any health care coverage?',['Yes','No'])
AnyHealthcare = 1.0 if AnyHealthcare  == 'Yes' else 0.0

NoDocbcCost = st.radio('Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?',['Yes','No'])
NoDocbcCost = 1.0 if NoDocbcCost == 'Yes' else 0.0

GenHlth = st.slider('Would you say that in general your health is: scale 1-5 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor',1,5)
GenHlth = float(GenHlth)

MentHlth = st.slider('Days of poor mental health in past 30 days',0,30)
MentHlth = float(MentHlth)

PhysHlth = st.slider('Days of physical illness or injury days in past 30 days',0,30)
PhysHlth = float(PhysHlth)

DiffWalk = st.radio('Do you have serious difficulty walking or climbing stairs?',['Yes','No'])
DiffWalk = 1.0 if DiffWalk == 'Yes' else 0.0

Sex = st.selectbox('What is your gender?',('Male','Female'))
Sex = 1.0 if Sex == 'Male' else 0.0

Age_Array = ['Age 18 to 24',
                        'Age 25 to 29',
                        'Age 30 to 34',
                        'Age 35 to 39',
                        'Age 40 to 44',
                        'Age 45 to 49',
                        'Age 50 to 54',
                        'Age 55 to 59',
                        'Age 60 to 64',
                        'Age 65 to 69',
                        'Age 70 to 74',
                        'Age 75 to 79',
                        'Age 80 or older']
Age = st.selectbox('What is your age?',(Age_Array))
for index, content in enumerate(Age_Array):
    if content == Age:
        Age = float(index)
        break

Education_Array = ['Never attended school or only kingdergarten',
                        'Elementary school',
                        'Some high school',
                        'High school graduate',
                        'Some college or technical school',
                        '4 years college or higher']
Education = st.selectbox('What is your education level?',(Education_Array))
for index, content in enumerate(Education_Array):
    if content == Education:
        Education = float(index)
        break

Income_Array = ['Less than $10,000',
                      '$10,000 to less than $15,000',
                      '$15,000 to less than $20,000',
                      '$20,000 to less than $25,000',
                      '$25,000 to less than $35,000',
                      '$35,000 to less than $50,000',
                      '$50,000 to less than $75,000',
                      '$75,000 or more']
Income = st.selectbox('What is your income level?',(Income_Array))
for index, content in enumerate(Income_Array):
    if content == Income:
        Income = float(index)
        break

row_answer = np.array([HighBP, HighChol, CholCheck, BMI, Smoker,
       Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,
       HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth,
       MentHlth, PhysHlth, DiffWalk, Sex, Age, Education,Income])
input_df = pd.DataFrame([row_answer])

filename = 'LightGBM_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def predict():
    result = loaded_model.predict(input_df)
    if result == 1.0:
        st.warning('You are at risk of diabetes :warning:')
    else:
        st.success('No risk of disbetes :thumbsup:')

st.button('Predict',on_click = predict)