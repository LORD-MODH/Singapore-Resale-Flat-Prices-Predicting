import streamlit as st
import pandas as pd
from model import load_model, predict
from data_preprocessing import preprocess_input_data

model = load_model('resale_price_model.pkl')

st.title('Singapore Resale Flat Prices Prediction')

town = st.selectbox('Select Town', ['Ang Mo Kio', 'Bedok', 'Bishan', 'Bukit Batok', 'Bukit Merah', 'Bukit Panjang', 'Bukit Timah', 'Central Area', 'Choa Chu Kang', 'Clementi', 'Geylang', 'Hougang', 'Jurong East', 'Jurong West', 'Kallang/Whampoa', 'Marine Parade', 'Pasir Ris', 'Punggol', 'Queenstown', 'Sembawang', 'Sengkang', 'Serangoon', 'Tampines', 'Toa Payoh', 'Woodlands', 'Yishun'])
flat_type = st.selectbox('Select Flat Type', ['1-room', '2-room', '3-room', '4-room', '5-room', 'Executive', 'Multi-Generation'])
storey_range = st.selectbox('Select Storey Range', ['01-03', '04-06', '07-09', '10-12', '13-15', '16-18', '19-21', '22-24', '25-27', '28-30', '31-33', '34-36', '37-39', '40-42', '43-45', '46-48', '49-51'])
floor_area_sqm = st.number_input('Enter Floor Area (sqm)', min_value=20, max_value=250, value=100)
lease_commence_date = st.number_input('Enter Lease Commence Date', min_value=1960, max_value=2023, value=2000)

if st.button('Predict'):
    input_data = pd.DataFrame([[town, flat_type, storey_range, floor_area_sqm, lease_commence_date]], columns=['town', 'flat_type', 'storey_range', 'floor_area_sqm', 'lease_commence_date'])
    input_data = preprocess_input_data(input_data)
    prediction = predict(model, input_data)
    st.write(f'Estimated Resale Price: ${prediction[0]:,.2f}')
