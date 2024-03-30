# """
# Project     :   Linkscribe
# Package     :   home
# Description :   This package sets Frontend of the LinkScribe app
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 28-03-2024      jdmunoz         Creation
# *********************************************************
# """

# Libraries 
import streamlit as st
import requests
import json
import time
import os
import subprocess
# ------

# Setting the API url from the container LinkScribe-backend:latest
#API_URL = os.getenv('API_URL', 'http://localhost:8080')
#print("API_URL", API_URL)

# For streamlit deployment 
subprocess.run(['sh', 'Frontend/script.sh'])
subprocess.run(['python', 'Backend/main.py'])
API_URL="http://localhost:8080" 

# Text constants
Title = 'LinkScribe 📝'
home_text = 'Welcome to LinkScribe the app that allows you to fast research web content using ML (Machine Learning based model 🤖) to classifying any webpage into a general subject so you only choose the ones you are really interested about.'
input_request_tx = 'Write the URL of the web page you wish to process'
about_title = '✍🏼 About'
aboutText1 = 'LinkScribe Project 📝 was born as a requirement for the AI Specialization Course from Universidad Autonoma de Occidente Cali'
aboutText2 = 'But we should mention that this is the first of many FullStack projects that implement ML-DL 🤖 models developed as open source with the given goals of learning, expand portfolio and create useful apps for the community.'
space = ''
# ---------

# Private Methods


# """
# Project     :   Linkscribe
# Package     :   home
# method      :   LS_model 
# Description :   This method calls the Backend API to use the ML-model 
# Inputs      :   url --> target URL    
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 28-03-2024      jdmunoz         Creation
# *********************************************************
# """
def LS_model(url):

    # setting the api with the model
    back_url = f"{API_URL}/LScribe-Model/predict"

    # input URL
    payload = json.dumps({
        "inURL":url
    })

    headers = {
    'Content-Type': 'application/json'
    }

    # Calling the API 
    response = requests.request("POST", back_url, headers=headers, data=payload)
    response = response.json()
    onuPrediction = response.get("prediction")
    return str(onuPrediction[0])


# """
# Project     :   Linkscribe
# Package     :   home
# method      :   LS_title 
# Description :   This method calls the Backend API return the Title 
#                 of the target URL 
# Inputs      :   url --> target URL    
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 28-03-2024      jdmunoz         Creation
# *********************************************************
# """
def LS_title(url):
    # setting the api with the model
    back_url = f"{API_URL}/webInfo/title"

    # input URL
    payload = json.dumps({
        "inURL":url
    })

    headers = {
    'Content-Type': 'application/json'
    }

    # Calling the API     
    response = requests.request("POST", back_url, headers=headers, data=payload)
    
    try:
        response = response.json()
    except ValueError:
        st.error('There was an error with the url please check the expelling and try again ', icon="🚨")

    onuTitle = response.get("Title")
    return str(onuTitle[0:])


# """
# Project     :   Linkscribe
# Package     :   home
# method      :   LS_Image 
# Description :   This method calls the Backend API return the preview image 
#                 of the target URL 
# Inputs      :   url --> target URL    
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 28-03-2024      jdmunoz         Creation
# *********************************************************
# """
def LS_Image(url):
    # setting the api with the model
    back_url = f"{API_URL}/webInfo/image"

    # input URL
    payload = json.dumps({
        "inURL":url
    })

    # Calling the API 
    response = requests.request("POST", back_url, data=payload, )
    onuImage = response.content
    return onuImage


# """
# Project     :   Linkscribe
# Package     :   home
# method      :   clear_form 
# Description :   Clear the input field   
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 28-03-2024      jdmunoz         Creation
# *********************************************************
# """
def clear_form():
    st.session_state["inuText"] = ""


# """
# Project     :   Linkscribe
# Package     :   home
# method      :   Execution 
# Description :   This method calls the Private methods to execute the app   
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 28-03-2024      jdmunoz         Creation
# *********************************************************
# """
def Execution():
   
    # setting the txt_input widget
    inURL = st.text_input('URL 👇', key="inuText", placeholder=input_request_tx)

    # Setting 2 columns
    left_column, right_column = st.columns(2)

    # Setting button    

    left_clicked = left_column.button('Classify') 

    st.divider()

    if left_clicked:        

        with st.spinner("Getting URL data ..."):
            title   = LS_title(inURL)   
            time.sleep(0.5)    

        st.write('The title of the webpage is:')
        st.subheader(title)
        st.divider()

        with st.spinner("Classifying URL ..."): 
            result  = LS_model(inURL)
            time.sleep(0.5)   

        st.write('The subject is:')
        st.subheader(result) 
        st.divider() 
            
        with st.spinner("Creating preview ..."):            
            Image   = LS_Image(inURL)
            time.sleep(0.5)

        st.write('Here´s a preview for you:')
        st.image(Image)

        # Clear the input 
        right_column.button('Clear', on_click= clear_form)

    
# """
# Project     :   Linkscribe
# Package     :   home
# method      :   about 
# Description :   This method shows the relevant about info  
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 28-03-2024      jdmunoz         Creation
# *********************************************************
# """
def about():
    # About Title 
    st.sidebar.title(about_title)
    st.sidebar.write(aboutText1)
    st.sidebar.write(space)
    st.sidebar.write(aboutText2)



# """
# Project     :   Linkscribe
# Package     :   home
# method      :   app 
# Description :   Principal Frontend method that set up the app  
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 28-03-2024      jdmunoz         Creation
# *********************************************************
# """
def app():  

    # Page configuration 
    st.set_page_config(
        page_title='LinkScribe Home Page', 
        page_icon='🤖', 
        layout='wide', 
        initial_sidebar_state='auto'
        )

    # Printing the default text
    st.title(Title)
    st.write(home_text)
    st.write('')

    # calling the widgets method
    Execution()
    about()

# Executing the app 
if __name__ == '__main__':
    app()
