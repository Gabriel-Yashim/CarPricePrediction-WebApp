# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 00:09:17 2023

@author: Gabriel Yashim
"""

import numpy as np 
import pickle
import streamlit as st


model = pickle.load(open('C:/Users/SHOPINVERSE/Documents/GitHub/CarPricePrediction-WebApp/GradientBoost.pkl', 'rb'))


st.title('Car Price Prediction System')
html_temp = """
    <h3 style="color:white;text-align:center;">By Gabriel Yashim</h3>
    <div style="background-color:pearl;padding:10px;margin-bottom:3rem">
        <p style="text-align:justify;">
            Welcome to this simple Car Price Prediction System. The system can predict the price of a car (in Million ₦) given some features. <br>
            The objective is to predict the price (Amount (Million Naira) the company should sell a car based on the available data (Location, Maker, Model, Year, Colour, Amount (Million Naira), Type, Distance). The objective is the predict the selling price.
        </p>  
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)


# Dictionary to map locations to integer values
location_mapping = {
    "":"",
    "Abuja": 0,
    "Ibadan": 1,
    "Lagos": 2
}

# Dictionary to map maker to integer values
maker_mapping = {
    "":"",
     'Acura':0,
     'Audi':1,
     'BAW':2,
     'BMW':3,
     'Bentley':4,
     'Brabus':5,
     'Buick':6,
     'Cadillac':7,
     'Chevrolet':8,
     'Chrysler':9,
     'Citroen':10,
     'Dodge':11,
     'Ferrari':12,
     'Fiat':13,
     'Ford':14,
     'GAC':15,
     'GMC':16,
     'Honda':17,
     'Hummer':18,
     'Hyundai':19,
     'IVM':20,
     'Infiniti':21,
     'JAC':22,
     'Jaguar':23,
     'Jeep':24,
     'Kia':25,
     'King':26,
     'Lamborghini':27,
     'Land Rover':28,
     'Lexus':29,
     'Lincoln':30,
     'MG':31,
     'Maserati':32,
     'Mazda':33,
     'Mercedes-Benz':34,
     'Mini':35,
     'Mitsubishi':36,
     'Nissan':37,
     'Opel':38,
     'Peugeot':39,
     'Pontiac':40,
     'Porsche':41,
     'Renault':42,
     'Rolls-Royce':43,
     'Rover':44,
     'Saab':45,
     'Saturn':46,
     'Scion':47,
     'Skoda':48,
     'Subaru':49,
     'Suzuki':50,
     'Tata':51,
     'Toyota':52,
     'Volkswagen':53,
     'Volvo':54
}

# Dictionary to map color to integer values
color_mapping = {
    "":"",
     'Beige':0,
     'Black':1,
     'Blue':2,
     'Brown':3,
     'Burgandy':4,
     'G':5,
     'Gold':6,
     'Gray':7,
     'Green':8,
     'Ivory':9,
     'Mica':10,
     'Orange':11,
     'Pearl':12,
     'Pink':13,
     'Purple':14,
     'Red':15,
     'Silver':16,
     'Teal':17,
     'Violet':18,
     'White':19,
     'Yellow':20
}

# Dictionary to map type to integer values
type_mapping = {
    "":"",
    'Brand New':0,
    'Foreign Used':1,
    'Nigerian Used':2
}


# Dropdown select box
selected_location = st.selectbox("Select Location:", list(location_mapping.keys()))
selected_maker = st.selectbox("Select the Brand:", list(maker_mapping.keys()))
year = st.text_input("Enter the Year of Production")
selected_color = st.selectbox("Select the Color:", list(color_mapping.keys()))
selected_type = st.selectbox("Select the car type:", list(type_mapping.keys()))
distance = st.text_input("Enter the distance the car has travelled (km):")

# storing the selected values in different variables    
location_value = location_mapping[selected_location]
maker_value = maker_mapping[selected_maker]
color_value = color_mapping[selected_color]
type_value = type_mapping[selected_type]


pred = ''

result = ''


if st.button('Submit'):
    pred = model.predict([[location_value, maker_value, year, color_value, type_value, distance]])
        
    st.write(f"The is worth  ₦{pred[0]:.2f} million")
    




