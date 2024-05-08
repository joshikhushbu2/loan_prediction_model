import streamlit as st
import pickle
import pandas as pd

with open ('loan_prediction_model.pkl','rb') as f:
    model = pickle.load(f)

def predict_loan_status(data):
    prediction=model.predict(data)
    return prediction

def main():
    st.title("Loan Prediction") 
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Loan Prediction </h2>   
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    loan_amount = st.number_input("Loan Amount")
    applicant_income = st.number_input("Applicant Income")
    coapplicant_income = st.number_input("CoApplicant Income")
    loan_term = st.number_input("Loan Term (Months)")
    credit_history = st.number_input("Credit History")

    result=""

    input_data = pd.DataFrame({'LoanAmount':[loan_amount],
                               'ApplicantIncome':[applicant_income],
                               'CoApplicantIncome':[coapplicant_income],
                               'LoanTerm':[loan_term],
                               'CreditHistory':[credit_history],})

    if st.button("Predict"):
        result=predict_loan_status(input_data)
    st.success('The loan status is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

main()
