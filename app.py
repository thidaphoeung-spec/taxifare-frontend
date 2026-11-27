import streamlit as st
import requests
import datetime
from dateutil.relativedelta import relativedelta

"""
# Taxifare Predictor
"""

st.markdown(
    """

    """)

"""
## Please select the characteristics of the taxi ride for which you want a fare prediction
"""

# 1. Récupération de la date et de l'heure via les widgets
date_choisie = st.date_input(
    "Select a date for the taxi ride :",
    value=datetime.date.today(),
    min_value=datetime.date(2000, 1, 1),
    max_value=datetime.date.today() + relativedelta(months=1),
    format="DD/MM/YYYY"
)
heure_choisie = st.time_input(
    "Select a time for the taxi ride :",
    value=datetime.time(7, 0),
    step=datetime.timedelta(minutes=1)
)

# 2. Combinaison et ajout du fuseau horaire UTC
dt_utc = datetime.datetime.combine(
    date_choisie, heure_choisie, tzinfo=datetime.timezone.utc
)

# 3. Formatage exact en chaîne de caractères
pickup_datetime = dt_utc.strftime("%Y-%m-%d %H:%M:%S %Z")

pickup_longitude = st.number_input(
    "Select a longitude for the taxi ride pickup :",
    min_value=-180.000000,
    max_value=180.000000,
    value=0.000000,
    step=0.000001
)
pickup_latitude = st.number_input(
    "Select a latitude for the taxi ride pickup :",
    min_value=-90.000000,
    max_value=90.000000,
    value=0.000000,
    step=0.000001
)
dropoff_longitude = st.number_input(
    "Select a longitude for the taxi ride dropoff :",
    min_value=-180.000000,
    max_value=180.000000,
    value=0.000000,
    step=0.000001
)
dropoff_latitude = st.number_input(
    "Select a latitude for the taxi ride dropoff :",
    min_value=-90.000000,
    max_value=90.000000,
    value=0.000000,
    step=0.000001
)
passenger_count = st.number_input(
    "Select the number of passengers :",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

url_api = "https://taxifare-api-gm5cveuyqa-ew.a.run.app/"
api_dict = {
    "pickup_datetime" : pickup_datetime,
    "pickup_longitude" : pickup_longitude,
    "pickup_latitude" : pickup_latitude,
    "dropoff_longitude" : dropoff_longitude,
    "dropoff_latitude" : dropoff_latitude,
    "passenger_count" : passenger_count
}
url_request = f"{url_api}predict?pickup_datetime={api_dict['pickup_datetime']}&pickup_longitude={api_dict['pickup_longitude']}&pickup_latitude={api_dict['pickup_latitude']}&dropoff_longitude={api_dict['dropoff_longitude']}&dropoff_latitude={api_dict['dropoff_latitude']}&passenger_count={api_dict['passenger_count']}"
response = requests.get(url_request, timeout=100)
response.raise_for_status()
response_api = response.json()

'''
## Fare prediction
'''
f"{response_api['fare']:.2f}"
