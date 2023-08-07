import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='Employee Attrition & Performance - EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('Employee Attrition Prediction')

    # Streamlit sub header
    st.subheader('EDA untuk analisa Dataset IBM HR Analytics Employee Attrition & Performance')


    # Menambahkan Deskripsi
    st.write('Page ini dibuat oleh _Zidny Yasrah Sallum_')
    st.write('## Dataframe Quick Peek')

    # Show DataFrame
    data = pd.read_csv('https://raw.githubusercontent.com/zidnyyasrah/Employee-Attrition/main/dataset.csv')
    st.dataframe(data)
    st.markdown('---')

    # Membuat barplot
    st.write('#### Plot Age')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(x='Age', data=data,kde=True,hue='Attrition')
    st.pyplot(fig)


    # Membuat Histogram Berdasarkan Input User
    st.write('#### Histogram on Various Feature')
    choice = st.radio('Select Columns : ', ('DistanceFromHome','YearsAtCompany','MonthlyIncome','PercentSalaryHike','YearsSinceLastPromotion','TotalWorkingYears'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[choice], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat plotly plot
    st.write('#### Plotly Plot - Age | Time')
    fig = px.scatter(data, x='YearsAtCompany', y='MonthlyIncome', hover_data=['Attrition'])
    st.plotly_chart(fig)

if __name__ == '__main__':
    run()