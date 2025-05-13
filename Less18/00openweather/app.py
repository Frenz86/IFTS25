import streamlit as st
import pandas as pd
import requests

import os
from dotenv import load_dotenv
load_dotenv('.env')
API_key : str = os.getenv('api_key')

#URL

def getweather(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    result = requests.get(url) # alternativa f string
    if result:
        json = result.json()
        #st.write(json)
        country = json['sys']['country']
        temp = json['main']['temp'] - 273.15 # to °C
        temp_feels = json['main']['feels_like'] - 273.15 # to °C
        humid = json['main']['humidity']
        pressure = json['main']['pressure']
        wind = json['wind']['speed']
        icon = json['weather'][0]['icon']
        lon = json['coord']['lon']
        lat = json['coord']['lat']
        des = json['weather'][0]['description']
        res = [country, round(temp,1),round(temp_feels,1),humid,lon,lat,icon,des,pressure,wind]
        return res , json
    else:
        print("errore di ricerca!")

# #HISTORICAL DATA deprecated
# def get_hist_data(lat,lon,start):
#     url_coord = f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={start}&appid={API_key}'
#     res = requests.get(url_coord)
#     data = res.json()
#     temp = []
#     for hour in data["hourly"]:
#         t = hour["temp"]
#         temp.append(t)     
#     return data , temp

####################################################################################
####################################################################################
def main():
    # st.title('Open Weather API')
    st.markdown('https://openweathermap.org/api') 

    image1 = 'sfondo.jpg'
    st.image(image1, caption='Open Weather API', use_container_width =True)

    col1, col2 = st.columns(2)
    with col1:
        city_name = st.text_input("Inserisci nome città")

    with col2:  
        if city_name:
            res , json = getweather(city_name)
            #st.write(res)
            st.success('T Attuale (°C):  ' + str(round(res[1],2)))
            st.info('T Percepita (°C):  ' + str(round(res[2],2)))
            st.info('Umidità (%):  ' + str(round(res[3],2)))
            st.info('Pressione (hPa):  ' + str(res[8]))
            st.info('Vento (m/s):  ' + str(res[-1]))
            st.subheader('Descrizione:  ' + res[7])

    if city_name:        
        # show_hist = st.expander(label = 'Ultimi 5 giorni')
        # with show_hist:
        #     start_date_string = st.date_input('Data corrente')
        #     date_df = []
        #     max_temp_df = []
        #     for i in range(5):
        #         date_Str = start_date_string - timedelta(i)
        #         start_date = datetime.strptime(str(date_Str),"%Y-%m-%d")
        #         timestamp_1 = datetime.timestamp(start_date)
        #         his , temp = get_hist_data(res[5],res[4],int(timestamp_1))
        #         date_df.append(date_Str)
        #         max_temp_df.append(max(temp) - 273.15) # to °C
        #     df = pd.DataFrame() # empty
        #     df['Date'] = date_df
        #     df['Max temp'] = max_temp_df
        #     df['Max temp'] = df['Max temp'].astype(int)
        #     st.table(df)
        st.map(pd.DataFrame({'lat' : [res[5]] , 'lon' : [res[4]]},columns = ['lat','lon']))

if __name__ == '__main__':
    main()