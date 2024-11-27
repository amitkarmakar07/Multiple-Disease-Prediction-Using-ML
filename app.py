import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import os

st.set_page_config(page_title="Mulitple Disease Prediction",layout="wide", page_icon="chart_with_upwards_trend")

#loading the models

working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open('diabetes_model.pkl','rb'))
with open('heart_model.pkl', 'rb') as file:
         heart_disease_model = pickle.load(file, encoding='latin1') 
with open('kidney_model.pkl', 'rb') as file:
         kidney_diseease_model = pickle.load(file, encoding='latin1')

# VALUES FOR DIABETES ENCODING COLUMS
NewBMI_Overweight=0
NewBMI_Underweight=0
NewBMI_Obesity_1=0
NewBMI_Obesity_2=0 
NewBMI_Obesity_3=0
NewInsulinScore_Normal=0 
NewGlucose_Low=0
NewGlucose_Normal=0 
NewGlucose_Overweight=0
NewGlucose_Secret=0


#creating sidebar

with st.sidebar:
        selected = option_menu("Mulitple Disease Prediction",
                    ['Diabetes Prediction','Heart Disease Prediction','Kidney Disease Prediction'],
                    menu_icon='hospital-fill',
                    icons=['activity','heart','person'],
                    default_index=0)
        
# DIABETES PREDICTION        
if selected=='Diabetes Prediction':
        st.title("Diabetes Prediction Using Machine Learing")
        col1,col2,col3=st.columns(3)

        with col1:
            Pregnancies = st.text_input("Number of Pregnancies")
        with col2:
            Glucose = st.text_input("Glucose Level")
        with col3:
            BloodPressure = st.text_input("BloodPressure Value")
        with col1:
            SkinThickness = st.text_input("SkinThickness Value")
        with col2:
            Insulin = st.text_input("Insulin Value")
        with col3:
            BMI = st.text_input("BMI Value")
        with col1:
            DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction Value")
        with col2:
            Age = st.text_input("Age")
        diabetes_result = ""
        if st.button("Diabetes Test Result"):
 
                #checking any null value input

                input = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
                    BMI,DiabetesPedigreeFunction,Age]
                if any(x == "" or x is None for x in input): 
                    st.error("Please enter all the required values.")

                else :     
                    # encoding columns
                    if float(BMI)<=18.5:
                        NewBMI_Underweight = 1
                    elif 18.5 < float(BMI) <=24.9:
                        pass
                    elif 24.9<float(BMI)<=29.9:
                        NewBMI_Overweight =1
                    elif 29.9<float(BMI)<=34.9:
                        NewBMI_Obesity_1 =1
                    elif 34.9<float(BMI)<=39.9:
                        NewBMI_Obesity_2=1
                    elif float(BMI)>39.9:
                        NewBMI_Obesity_3 = 1
                    
                    if 16<=float(Insulin)<=166:
                        NewInsulinScore_Normal = 1

                    if float(Glucose)<=70:
                        NewGlucose_Low = 1
                    elif 70<float(Glucose)<=99:
                        NewGlucose_Normal = 1
                    elif 99<float(Glucose)<=126:
                        NewGlucose_Overweight = 1
                    elif float(Glucose)>126:
                        NewGlucose_Secret = 1

                    user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
                        BMI,DiabetesPedigreeFunction,Age, NewBMI_Underweight,
                        NewBMI_Overweight,NewBMI_Obesity_1,
                        NewBMI_Obesity_2,NewBMI_Obesity_3,NewInsulinScore_Normal, 
                        NewGlucose_Low,NewGlucose_Normal, NewGlucose_Overweight,
                        NewGlucose_Secret]
                    
                    
                    user_input = [float(x) for x in user_input]
                    prediction = diabetes_model.predict([user_input])
                    probability = diabetes_model.predict_proba([user_input])
                    percentage = probability[0][1] * 100

                    if prediction[0]==1:
                        diabetes_result = f"The person has diabetes with a probability of {percentage:.2f}%."
                    else:
                        diabetes_result = f"The person does not have diabetes with a probability of {(100 - percentage):.2f}%."
                    st.success(diabetes_result)


# HEART DISEASE PREDICTION

if selected=='Heart Disease Prediction':
        st.title("Heart Disease Prediction Using Machine Learing")
        col1,col2,col3=st.columns(3)
        
        with col1:
            age = st.text_input("Age")
        with col2:
            sex = st.selectbox("Sex", options=["Male", "Female"], index=0)
            sex = 1 if sex == "Male" else 0
        with col3:
            cp = st.selectbox("cp", options=["Normal", "Intermediate","Severe"], index=0)
            if cp == "Normal":
                    cp = 0
            elif cp == "Intermediate":
                cp = 1
            elif cp == "Severe":
                cp = 2
        with col1:
            trestbps = st.text_input("Resting Blood Pressure")
        with col2:
            chol = st.text_input("Serum Cholestroal in mg/dl")
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('Thal')
        
        heart_disease_result = ""

        if st.button("Heart Disease Test Result"):
            user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
            #chekcing null values as input
            if any(x == "" or x is None for x in user_input): 
                    st.error("Please enter all the required values.")
            else:
                user_input = [float(x) for x in user_input]
                prediction = heart_disease_model.predict([user_input])
                probability = heart_disease_model.predict_proba([user_input])
                percentage = probability[0][1] * 100

                if prediction[0]==1:
                    heart_disease_result = f"The person has heart disease with a probability of {percentage:.2f}%."
                else:
                    heart_disease_result = f"The person does not have heart disease with a probability of {(100 - percentage):.2f}%."
                st.success(heart_disease_result)

#KIDNEY DISEASE PREDICTION

if selected=='Kidney Disease Prediction':
        st.title("Kidney Disease Prediction using Machine Learning")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
                age = st.text_input('Age')
        with col2:
                blood_pressure = st.text_input('Blood Pressure')
        with col3:
                specific_gravity = st.text_input('Specific Gravity')
        with col4:
                albumin = st.text_input('Albumin')
        with col5:
                sugar = st.text_input('Sugar')
        with col1:
                red_blood_cells = st.text_input('Red Blood Cell')
        with col2:
                pus_cell = st.text_input('Pus Cell')
        with col3:
                pus_cell_clumps = st.text_input('Pus Cell Clumps')
        with col4:
                bacteria = st.text_input('Bacteria')
        with col5:
                blood_glucose_random = st.text_input('Blood Glucose Random')
        with col1:
                blood_urea = st.text_input('Blood Urea')
        with col2:
                serum_creatinine = st.text_input('Serum Creatinine')
        with col3:
                sodium = st.text_input('Sodium')
        with col4:
                potassium = st.text_input('Potassium')
        with col5:
                haemoglobin = st.text_input('Haemoglobin')
        with col1:
                packed_cell_volume = st.text_input('Packet Cell Volume')
        with col2:
                white_blood_cell_count = st.text_input('White Blood Cell Count')
        with col3:
                red_blood_cell_count = st.text_input('Red Blood Cell Count')
        with col4:
                hypertension = st.text_input('Hypertension')
        with col5:
                diabetes_mellitus = st.text_input('Diabetes Mellitus')
        with col1:
                coronary_artery_disease = st.text_input('Coronary Artery Disease')
        with col2:
                appetite = st.text_input('Appetitte')
        with col3:
                peda_edema = st.text_input('Peda Edema')
        with col4:
                aanemia = st.text_input('Aanemia')
        
        kindey_disease_result = ''

        if st.button("Kidney's Test Result"):
            user_input = [age, blood_pressure, specific_gravity, albumin, sugar,
            red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
            blood_glucose_random, blood_urea, serum_creatinine, sodium,
            potassium, haemoglobin, packed_cell_volume,
            white_blood_cell_count, red_blood_cell_count, hypertension,
            diabetes_mellitus, coronary_artery_disease, appetite,
            peda_edema, aanemia]
              
            #checking null values
            
            if any(x == "" or x is None for x in user_input): 
                    st.error("Please enter all the required values.")
            else :
                user_input = [float(x) for x in user_input]
                prediction = kidney_diseease_model.predict([user_input])
                probability = kidney_diseease_model.predict_proba([user_input])
                percentage = probability[0][1] * 100

                if prediction[0]==1:      
                        kindey_disease_result = f"The person has Chronic Kidney Disease with a probability of {percentage:.2f}%."
                else:
                    kindey_disease_result = f"The person does not have Chronic Kidney Disease with a probability of {(100 - percentage):.2f}%."
                st.success(kindey_disease_result)

