import streamlit as st
import joblib

clf=joblib.load('loan.joblib')


st.title('LOAN APP RCE BY CHANDANA')
g=st.number_input('Enter Gender 0:Male 1:Female')
m=st.number_input('Enter Maritial Status 0:No 1:Yes')
ai=st.number_input('Enter Applicant income in Thousands')
la=st.number_input('Enter loan amount in Thousands')

if st.button('PREDICT'):
    prediction=clf.predict([[g,m,ai,la]])
    if prediction=='Y':
        st.text('YOUR LOAN IS APPROVED')
    else:
        st.text('YOUR LOAN IS REJECTED')
