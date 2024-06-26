import streamlit as st
import plotly.express as px
from backend import get_data


st.set_page_config(page_title="Weather Forecast App",
    page_icon="sun_with_face",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "## This is an *extremely* cool app!"
    }
)

st.title("Weather Forecast for the Next Days")


place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


if place:
    # Get temperature data
    
    try:
        filtered_Data = get_data(place, days)

        if option == "Temperature":
            # Create a temperature plit
            temperature = [dict['main']['temp'] / 10 for dict in filtered_Data]
            dates = [dict["dt_txt"] for dict in filtered_Data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                    "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_Data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)

    except KeyError:
        st.warning("This city does not exist.")
