import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
#pages in python format
from pag import contacts, history, home,map, datavisualisation

st.set_page_config(
                    page_title="Template Project",
                    page_icon=Image.open("icon_site.png"),
                    layout="wide",
                    )

page = [
        "Home", 
        "History", 
        "Data Visualisation",
        "Maps", 
        "Contacts",
        ]

#bootstrap Icon
icons = [
        "bi-house", 
        "bi-hourglass-split", 
        "bi-card-image", 
        "bi-map",#"bi-geo-alt"
        "bi-envelope",
        ]


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
                        "title": title,
                        "function": function
                        })

    def main():
        with st.sidebar:
            app = option_menu(
                            menu_title = "Menu",
                            options = page,
                            icons = icons,
                            #orientation = "horizontal",
                            menu_icon = "bi-list",
                            default_index = 0,
                            styles = {
                                    "container": {"padding": "5!important", "background-color": "black"},
                                    "icon": {"color": "white", "font-size": "23px"},
                                    "nav-link": {"color": "white", "font-size": "20 px", "text-align": "left", "margin": "0px" },
                                    "nav-link-selected": {"color": "black", "background-color": "#9ac280"}
                                    }
                            )
        if app == page[0]:
            home.main()
        if app == page[1]:
            history.main()
        if app == page[2]:
            datavisualisation.main()
        if app == page[3]:
            map.main()
        if app == page[4]:
            contacts.main()

##########################################################################################

if __name__ == "__main__":
    MultiApp.main()  
