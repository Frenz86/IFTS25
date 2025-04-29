import streamlit as st
import folium
from folium import plugins
from streamlit_folium import folium_static

def main():

    st.title("Mappa di Roma - Punti di Interesse")
    roma_lat = 41.9028
    roma_lng = 12.4964

    # Creazione della mappa centrata su Roma
    m = folium.Map(location=[roma_lat, roma_lng], 
                zoom_start=12,
                tiles='CartoDB positron')

    # Aggiunta di alcuni punti di interesse principali
    landmarks = {
                "Colosseo": [41.8902, 12.4922],
                "Basilica San Pietro": [41.9022, 12.4539],
                "Pantheon": [41.8986, 12.4769],
                "Fontana di Trevi": [41.9009, 12.4833],
                "Piazza Navona": [41.8992, 12.4730]
                }

    marker_cluster = plugins.MarkerCluster(control=False)
    for name, coords in landmarks.items():
        folium.Marker(
                    coords,
                    popup=name,
                    icon=folium.Icon(color='red', icon='info-sign')
                    ).add_to(marker_cluster)

    m.add_child(marker_cluster)
    minimap = plugins.MiniMap()
    m.add_child(minimap)
    folium.LayerControl().add_to(m)
    # Visualizzazione con Streamlit
    folium_static(m, width=800, height=600)

if __name__ == "__main__":
    main()
    
