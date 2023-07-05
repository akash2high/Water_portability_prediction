import streamlit as st
import pickle
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

model = pickle.load(open('water_potablity.pkl', 'rb'))


# def preprocess_input(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity,
#        Organic_carbon, Trihalomethanes, Turbidity):
#     # Perform any preprocessing steps here
#     data = [[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity,
#        Organic_carbon, Trihalomethanes, Turbidity]]
#     values = data
#     return values


def predict(values):
    prediction = model.predict(values)
    return prediction


def main():
    html_title = """
    <h1 style="color:red;"><b><u>Water Potablity</u></b></h1>
    """
    st.markdown(html_title, unsafe_allow_html=True)

    ph = st.number_input("ph", min_value=0, step=1)
    Hardness = st.number_input("Hardness", min_value=0.0, step=0.1 )
    Solids = st.number_input("Solids", min_value=0.0, step=0.1)
    Chloramines = st.number_input("Chloramines", min_value=0.0, step=0.1)
    Sulfate = st.number_input("Sulfate", min_value=0, step=1)
    Conductivity = st.number_input("Conductivity", min_value=0, step=1)
    Organic_carbon = st.number_input("Organic_carbon", min_value=0, step=1)
    Trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, step=0.1)
    Turbidity = st.number_input("Turbidity", min_value=0.0, step=0.1)

    if st.button("Predict"):
        values = [[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity,
       Organic_carbon, Trihalomethanes, Turbidity]]

        prediction = predict(values)
        if prediction[0]==1:
          water = "Water IS POTABLE"
        else:
          water = "WATER IS NOT POTABLE"

        st.success(water)


if __name__ == '__main__':
    main()
