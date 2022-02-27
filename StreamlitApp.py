# Importing Libraries
import streamlit as st
import pickle
import numpy as np
import string
st.set_option('deprecation.showfileUploaderEncoding',False) 

# Loading a best model
model = pickle.load(open('randomforest.pkl', 'rb'))


def main():
    # Main Page - Title
    st.title('Bank Marketing Prediction')
    st.subheader('Bank Marketing Prediction on Subscription of Term Deposit')
    
    
    # Side Bar 
    st.sidebar.header('Project Overview')
    st.sidebar.text("It's a Machine Learning App that predicts whether a customer will subscribe for Term Deposit or Not based on various parameters.")
    st.sidebar.text('This Machine Learning Model is build over the real world data of Portuguese Bank')
    st.sidebar.header('Tools')
    st.sidebar.text('Streamlit')
    st.sidebar.text('Python')
    st.sidebar.text('Pandas')
    st.sidebar.text('Numpy')
    st.sidebar.text('Sklearn')
    st.sidebar.subheader('About the App')
    st.sidebar.text('Developed by Inbarasan Manivannan')
    
    # Input Boxes:
    # Client Information
    age = st.number_input("Age", 0, 100)
    st.write('0 - Admin, 1 - Blue-collar, 2 - Entrepreneur, 3 - Housemaid, 4 - Management, 5 - Retired, 6 - Self-employed, 7 - Services, 8 - Student, 9 - Technician, 10 - Unemployed, 11 - Unknown')
    job = st.number_input('Type of Job', 0, 11)
    st.write('0 - Divorced or Widowed, 1 - Married, 2 - Single')
    marital = st.number_input('Marital Status', 0, 2)
    education = st.number_input('Education Details(0 - Primary, 1 - Secondary, 2 - Teritary, 3 - Unknown)', 0, 3)
    default = st.number_input('Has Credit in Default? (0 - No, 1 - Yes)', 0,1)
    balance = st.number_input("Average Yearly balance in Euro's", 0, 1000000)   
    housing = st.number_input('Has Housing Loan (0 - No, 1 - Yes)', 0,1) 
    loan = st.number_input('Has Personal Loan (0 - No, 1 - Yes)', 0,1)
    
    # Last Contact of Current Campaign Information
    contact = st.number_input('Contact Communication Type (0 - Cellular, 1 - Telephone, 2 - Unknown)', 0,2)
    day = st.number_input('Last Contact day of the month', 0,31)
    month = st.number_input('Last Contact month of the Year (January - 0...Dec - 12)', 0,12)
    duration = st.number_input('Last Contact Duration in Seconds', 0,28800)
    
    # Campaigning Information
    campaign = st.number_input('Number of contacts performed during this campaign and for this client', 0, 63)
    pdays = st.number_input('Number of days that passed by after the client was last contacted from a previous campaign (-1 - Not Contacted)', -1, 1)
    previous = st.number_input('Number of contacts performed before this campaign and for this client', 0, 275)
    poutcome = st.number_input('Outcome of the previous marketing campaign (0 - Failure, 1 - Other, 2 - Success, 3 - Unknown)', 0,3)
    
    
    
    
    #Input List of values
    input = [[age, job, marital, education, default, balance, housing, loan, contact, day, month, duration, campaign, pdays, previous, poutcome]]

    
    
    # Output Show
    potential="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Potential Customer - will Subscribe</h2>
       </div>
    """
    not_potential="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> will not Subscribe</h2>
       </div>
    """


    if st.button("Predict"):
        output= model.predict(input)
        updated_res = output.flatten().astype(float)

        if output > 0.75:
            st.markdown(not_potential,unsafe_allow_html=True)
            st.write('Suggestion: ')
            st.write('We can suggest the Customer with some attractive benefits we can make them subscribe to TERM DEPOSIT. The Benefits like Tax Benefits, Easy Loan Aceeptance, Medical Insurance Coverage, etc., are the main reasons why the Customer want to subscribe for TERM DEPOSIT. So approaching with benefits and Futuristic Plans, we can make the Customer to subscribe for TERM DEPOSIT.')
            
        else:
            st.markdown(potential,unsafe_allow_html=True)
            st.write('Suggestion: ')
            st.write('By giving the above parameters, the probability of subscribing for TERM DEPOSIT is high. So the Customer will subscribe for TERM DEPOSIT')
    
if __name__ == '__main__':
    main()
    
