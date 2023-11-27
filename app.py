import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st

from table import TableDashboard

# Define the Streamlit app
def main():
    st.set_page_config(layout="wide")

    with open('style.css') as f:
        st.markdown(f'''
                    <style>
                        {f.read()}
                    </style>''',
                    unsafe_allow_html=True)

    df_day = pd.read_csv('day.csv')

    st.markdown("<h1 class='header-title'>BIKE SHARING DASHBOARD</h1>", unsafe_allow_html=True)

    table_dashboard = TableDashboard(df_day)

    month_year, year_season, year_weathersit = table_dashboard.start()

    with st.container():

        col1, col2 = st.columns([1, 1])

        with col1:

            st.markdown("<h1 class='title'>Total Counts per Month by Season</h1>", unsafe_allow_html=True)
            
            st.pyplot(year_season)
        
        with col2:
            
            st.markdown("<h1 class='title'>Total Counts per Month by Weathersit</h1>", unsafe_allow_html=True)
            
            st.pyplot(year_weathersit)

    with st.container():

        st.markdown("<h1 class='title'>Total Counts per Month by Year</h1>", unsafe_allow_html=True)
        
        st.pyplot(month_year)


# Run the Streamlit app
if __name__ == "__main__":
    main()
