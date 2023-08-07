import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Menggunakan joblib untuk meload model
pipeline = joblib.load('model.pkl')

def run():
    # Membuat Title
    st.title('Fill Your Data')
    with st.form('key=form_employee'):

 


        age = st.number_input('Age',value=25,help='Usia Karyawan')
        gender = st.radio('gender', (['Female','Male']))
        st.markdown('---')

        BusinessTravel = st.radio('BusinessTravel', (['Travel_Rarely','Travel_Frequently','Non-Travel']))
        DailyRate = st.number_input('Daily Rate', value=25,help='Daily Rate')
        Department = st.radio('Department', (['Sales','Research & Development','Human Resources']))
        DistanceFromHome = st.number_input('Distance From Home', min_value=20,max_value=90,value=25,help='Distance From Home')
        st.markdown('---')

        Education = st.radio('Education', (1,2,3,4,5))
        EducationField = st.radio('Education Field', (['Life Sciences','Medical','Marketing','Technical Degree','Human Resources','Other']))
        EnvironmentSatisfaction = st.radio('EnvironmentSatisfaction', (1,2,3,4,5))
        HourlyRate = st.number_input('Hourly Rate ', value=25,help='Hourly Rate')
        JobInvolvement = st.radio('Job Involvement', (1,2,3,4))
        JobLevel = st.radio('Job Involvement', (1,2,3,4,5))
        JobRole = st.radio('Job Role', (['Sales Executive', 'Research Scientist', 'Laboratory Technician',
       'Manufacturing Director', 'Healthcare Representative', 'Manager',
       'Sales Representative', 'Research Director', 'Human Resources']))
        JobSatisfaction = st.radio('Job Satisfaction', (1,2,3,4))
        MaritalStatus = st.radio('Marital Status ', (['Single', 'Married', 'Divorced']))
        MonthlyIncome = st.number_input('Monthly Income', value=25,help=' Monthly Income')
        MonthlyRate = st.number_input('Monthly Rate', value=25,help='Monthly Rate')
        NumCompaniesWorked = st.number_input('Number of Companies Worked', value=25)
        OverTime = st.radio('OverTime', (['Yes','No']))
        PercentSalaryHike = st.number_input('Percent Salary Hike', value=25,help='Percent Salary Hike')
        PerformanceRating = st.radio('Performance Rating', (3,4))
        RelationshipSatisfaction = st.radio('Relationship Satisfaction', (1,2,3,4))
        StockOptionLevel = st.radio('Relationship Satisfaction', (0,1,2,3))
        TrainingTimesLastYear = st.number_input('Training Times Last Year', value=25)
        WorkLifeBalance = st.radio('Work Life Balance', (1,2,3,4))
        YearsAtCompany = st.number_input('Years At Company', value=25)

        submitted = st.form_submit_button('Predict')

    # Membuat data inference baru
    data_inf = {
    'Age': age,
    'BusinessTravel': BusinessTravel,
    'DailyRate': DailyRate,
    'Department': Department,
    'DistanceFromHome': DistanceFromHome,
    'Education': Education,
    'EducationField': EducationField,
    'EnvironmentSatisfaction': EnvironmentSatisfaction,
    'Gender': gender,
    'HourlyRate': HourlyRate,
    'JobInvolvement': JobInvolvement,
    'JobLevel': JobLevel,
    'JobRole': JobRole,
    'JobSatisfaction': JobSatisfaction,
    'MaritalStatus': MaritalStatus,
    'MonthlyIncome': MonthlyIncome,
    'MonthlyRate': MonthlyRate,
    'NumCompaniesWorked': NumCompaniesWorked,
    'OverTime': OverTime,
    'PercentSalaryHike': PercentSalaryHike,
    'PerformanceRating': PerformanceRating,
    'RelationshipSatisfaction': RelationshipSatisfaction,
    'StockOptionLevel': StockOptionLevel,
    'TrainingTimesLastYear': TrainingTimesLastYear,
    'WorkLifeBalance': WorkLifeBalance,
    'YearsAtCompany': YearsAtCompany,
}

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:

            
        # Melakukan prediksi dengan model dari data baru
        prediksi = pipeline.predict(data_inf)
        prediksi = int(prediksi)
        value = ''
        if prediksi == 0:
            value = "You're Likely to stay"
        elif prediksi == 1:
            value = "Positive Attrition"
        st.write('# ', value)
        

if __name__ == '__main__':
   run()