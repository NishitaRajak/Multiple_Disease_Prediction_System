#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[3]:


import streamlit as st


# In[4]:


from streamlit_option_menu import option_menu


# In[ ]:





# In[8]:


with open("C:/Users/Asus/Desktop/Multiple Disease prediction system/saved models/diabetes_model.sav", 'rb') as file:
    diabetes_model = pickle.load(file)


# In[9]:


with open("C:/Users/Asus/Desktop/Multiple Disease prediction system/saved models/heart_model.sav", 'rb') as file:
    heart_disease_model = pickle.load(file)


# In[16]:


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                          'Heart Disease Prediction'],
                           icons = ['activity','heart-pulse'],
                          default_index = 0)


# In[14]:


if(selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction Using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

    
    
    
    
    
if(selected == 'Heart Disease Prediction'):
    st.title("Heart Disease Prediction Using ML")
    
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        male = st.number_input('Sex')
        
    with col2:
        
        age = st.number_input('Age')
        
    with col3:
        
        currentSmoker = st.number_input('current Smoking status')
        
    with col1:
        cigsPerDay = st.number_input('cigsPerDay')
        
    with col2:
        BPMeds = st.number_input('BPMeds')
        
    with col3:
        prevalentStroke = st.number_input('prevalentStroke')
        
    with col1:
        prevalentHyp = st.number_input('prevalentHyp')
        
    with col2:
        diabetes = st.number_input('diabetes')
        
    with col3:
        totChol = st.number_input('totChol')
        
    with col1:
        sysBP = st.number_input('sysBP')
        
    with col2:
        diaBP = st.number_input('diaBP')
        
    with col3:
        BMI = st.number_input('BMI')
        
    with col1:
        heartRate = st.number_input('heartRate')
    
    with col2:
        glucose = st.number_input('glucose')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]])                          
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)


# In[ ]:




